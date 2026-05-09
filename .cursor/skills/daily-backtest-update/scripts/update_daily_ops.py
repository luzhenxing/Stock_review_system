#!/usr/bin/env python3
"""
每日持仓更新工具
用法：
  python -X utf8 .cursor/skills/daily-backtest-update/scripts/update_daily_ops.py \
    --date 2026-05-09 \
    --total-assets 704788.01 \
    --available-cash 2318.01 \
    --holdings '[{"code":"600487","name":"亨通光电","position_pct":11.0,"cost":56.45,"price":77.27,"market_value":77270}]'
"""
import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path

PRINCIPAL = 500_000.0  # 本金（固定）

# 脚本在 .cursor/skills/daily-backtest-update/scripts/ 下，PROJECT_ROOT 为上4级
_HERE = Path(__file__).resolve()
PROJECT_ROOT = _HERE.parents[4]

# 允许环境变量覆盖（调试用）
if os.environ.get("PROJECT_ROOT"):
    PROJECT_ROOT = Path(os.environ["PROJECT_ROOT"])

DAILY_OPS_FILE = PROJECT_ROOT / "dailyOperations.txt"


# ── 解析上一条持仓记录 ─────────────────────────────────────────
def _parse_last_holdings(text: str) -> dict[str, float]:
    """返回 {股票名称: 仓位百分比数值}，取文件中最后一个日期块"""
    blocks = re.split(r"\n(?=\d{1,2}/\d{1,2}\b|\d{4}-\d{2}-\d{2}\b)", text.strip())
    if not blocks:
        return {}
    last_block = blocks[-1]
    m = re.search(r"【持仓状态】(.*?)(?=【|$)", last_block, re.DOTALL)
    if not m:
        return {}
    result: dict[str, float] = {}
    for line in m.group(1).splitlines():
        line = line.strip().lstrip("- ")
        if not line:
            continue
        name_m = re.match(r"(.+?)：持仓([\d.]+)%", line)
        if name_m:
            result[name_m.group(1).strip()] = float(name_m.group(2))
    return result


# ── 推算今日操作 ──────────────────────────────────────────────
def _calc_operations(prev: dict[str, float], curr: list[dict]) -> list[str]:
    curr_map = {h["name"]: h["position_pct"] for h in curr if not h.get("is_cash") and h["name"] != "现金"}
    ops: list[str] = []

    prev_names = set(prev.keys()) - {"现金"}
    curr_names = set(curr_map.keys())

    for name in sorted(prev_names - curr_names):
        ops.append(f"清仓{name}")

    for name in sorted(curr_names - prev_names):
        ops.append(f"建仓{name}（{curr_map[name]:.1f}%）")

    for name in sorted(prev_names & curr_names):
        delta = curr_map[name] - prev[name]
        if delta > 1.0:
            ops.append(f"{name}加仓{delta:+.1f}pp→{curr_map[name]:.1f}%")
        elif delta < -1.0:
            ops.append(f"{name}减仓{delta:+.1f}pp→{curr_map[name]:.1f}%")

    return ops if ops else ["无变动"]


# ── 构造追加文本 ───────────────────────────────────────────────
def _build_entry(date_str: str, total_assets: float, available_cash: float,
                 holdings: list[dict], operations: list[str]) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    header = f"{dt.month}/{dt.day}"

    pnl = total_assets - PRINCIPAL
    pnl_pct = pnl / PRINCIPAL * 100
    net_value = total_assets / PRINCIPAL
    sign = "+" if pnl >= 0 else ""

    fund_lines = [
        f"- 总资产：¥{total_assets:,.2f}",
        f"- 可用资金：¥{available_cash:,.2f}",
        f"- 本金：¥{PRINCIPAL:,.0f}",
        f"- 累计盈亏：{sign}¥{pnl:,.2f}（{sign}{pnl_pct:.2f}%）",
        f"- 净值：{net_value:.4f}",
    ]

    holding_lines = []
    for h in holdings:
        if h.get("is_cash") or h["name"] == "现金":
            holding_lines.append(f"- 现金：持仓{h['position_pct']:.1f}%")
        else:
            holding_lines.append(f"- {h['name']}：持仓{h['position_pct']:.1f}%，成本 {h['cost']}")

    op_lines = [f"- {'；'.join(operations)}；"]

    lines = [
        header, "",
        "【资金信息】", *fund_lines, "",
        "【持仓状态】", *holding_lines, "",
        "【今日操作】", *op_lines,
    ]
    return "\n".join(lines)


# ── 主程序 ────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="追加每日持仓记录")
    parser.add_argument("--date", required=True, help="日期 YYYY-MM-DD")
    parser.add_argument("--total-assets", type=float, required=True)
    parser.add_argument("--available-cash", type=float, required=True)
    parser.add_argument("--holdings", required=True, help="JSON 持仓列表")
    args = parser.parse_args()

    holdings: list[dict] = json.loads(args.holdings)

    prev: dict[str, float] = {}
    if DAILY_OPS_FILE.exists():
        prev = _parse_last_holdings(DAILY_OPS_FILE.read_text(encoding="utf-8"))

    operations = _calc_operations(prev, holdings)
    entry = _build_entry(args.date, args.total_assets, args.available_cash, holdings, operations)

    existing = DAILY_OPS_FILE.read_text(encoding="utf-8") if DAILY_OPS_FILE.exists() else ""
    sep = "\n\n" + "─" * 40 + "\n\n"
    new_content = (existing.rstrip() + sep + entry + "\n") if existing.strip() else entry + "\n"
    DAILY_OPS_FILE.write_text(new_content, encoding="utf-8")

    pnl = args.total_assets - PRINCIPAL
    print(f"✓ 已追加 {args.date} → {DAILY_OPS_FILE.name}")
    print(f"  今日操作：{'；'.join(operations)}")
    print(f"  累计盈亏：{'+'if pnl>=0 else ''}¥{pnl:,.2f}（{pnl/PRINCIPAL*100:.2f}%）  净值：{args.total_assets/PRINCIPAL:.4f}")


if __name__ == "__main__":
    main()
