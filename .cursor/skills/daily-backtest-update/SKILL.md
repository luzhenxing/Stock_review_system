---
name: daily-backtest-update
description: >-
  每日持仓回测更新工作流：解析持仓截图 → 更新 dailyOperations.txt → 跑无情操盘手回测（1年/2年）→ 拉取 MACD/白黄线信号
  → 生成操作建议 → 更新持仓总览看板 → 重启 Web 服务。
  当用户说"帮我更新回测"、"更新持仓"、"回测一下"、"看一下持仓"，或发送持仓截图时触发。
  不用于：单独查询行情、只修改看板文字、非持仓相关的回测。
  TRIGGER ON 更新回测 更新持仓 回测一下 看一下持仓 持仓截图。
---

# 每日持仓回测更新

## Purpose

解析用户当日持仓截图，自动完成日志记录、回测运行、技术信号拉取、操作建议生成、看板更新、Web 服务重启的完整闭环流程。

## When to use me

- 用户发送了持仓截图并说"帮我更新回测"
- 用户说"更新持仓"、"回测一下"、"看一下持仓"
- 用户每日收盘后需要记录当日持仓并获取操作建议

## When NOT to use me

- 仅查询某只股票的行情或 K 线（不需要更新持仓日志）
- 只修改 `持仓/仓位总览.md` 的文字描述，无新持仓数据
- 对历史日期做回测复盘（不写入 dailyOperations.txt）
- 非股票持仓相关的通用回测需求

## Inputs / Preconditions

Required:
- 持仓截图（含：证券代码、名称、数量、成本价、当前价、最新市值、账户总资产、余额/可用资金）
- 操作日期（YYYY-MM-DD，默认取今日）

Optional:
- 手动指定日期（用户明确说明时使用）

If missing：若截图字段不清晰，逐字段询问用户确认，不得推测数值。

## Workflow

### Step 1 — 解析持仓截图 — BLOCKING

从截图提取以下字段：

| 字段 | 来源列 |
|------|--------|
| 股票代码 | 证券代码列（6位数字） |
| 股票名称 | 证券名称列 |
| 持仓数量 | 证券数量列 |
| 成本价 | 成本价列 |
| 当前价 | 当前价列 |
| 市值 | 最新市值列 |
| 账户总资产 | 顶部"资产"字段 |
| 余额/可用资金 | 顶部"余额"或"可用"字段 |

计算各股仓位比例 = 市值 / 总资产 × 100%

Result：得到结构化持仓列表 + 资金信息，确认无误后进入 Step 2。

---

### Step 2 — 运行 update_daily_ops.py — BLOCKING

> `dailyOperations.txt` 的正确位置是 `WaveformTheory-Clean/`，必须通过环境变量 `PROJECT_ROOT` 指定，否则脚本会写到项目根目录。

PowerShell：
```powershell
cd "D:\Stock_review _system\WaveformTheory-Clean"
$env:PROJECT_ROOT = "D:\Stock_review _system\WaveformTheory-Clean"
$holdings = '<JSON>'
python -X utf8 "D:\Stock_review _system\.cursor\skills\daily-backtest-update\scripts\update_daily_ops.py" `
  --date "YYYY-MM-DD" `
  --total-assets <总资产> `
  --available-cash <余额> `
  --holdings $holdings
```

`--holdings` JSON 格式：
```json
[
  {"code": "600487", "name": "亨通光电", "position_pct": 11.0, "cost": 56.45, "price": 77.27, "market_value": 77270},
  {"name": "现金", "position_pct": 0.4, "is_cash": true}
]
```

Result：脚本输出 `✓ 已追加 YYYY-MM-DD`，`dailyOperations.txt` 新增本日记录（含【资金信息】【持仓状态】【今日操作】）。

---

### Step 3 — 跑无情操盘手回测（1年 + 2年）— CONDITIONAL

> 仅对有代码的股票（非现金）执行。

```python
import sys, json, os
sys.path.insert(0, '脚本')
os.environ['no_proxy'] = '*'
import backtest_ruthless as br

holdings = [("code", "name"), ...]   # 从 Step 1 获取
for y in (1, 2):
    for code, name in holdings:
        r = br.backtest_ruthless(code, name, capital=10000, years=y)
```

Result：每只股票获得 1年/2年 回测收益率，用于 Step 5 建议生成。

---

### Step 4 — 拉取 MACD + 白黄线状态

```python
from fetch_wave_data import fetch_kline, calc_macd, calc_ema, calc_sma
# 白线 = calc_dema(closes, 10)；黄线 = calc_quad_ma(closes)
# 判断：金叉/死叉/多头/空头；白>黄 / 白<黄
```

Result：每只股票得到当前 MACD 状态 + 白/黄线位置关系。

---

### Step 5 — 生成操作建议

基于回测结果 + 当前信号，按优先级给出：

- 🔴 **减仓**：白<黄线 + 2年回测负收益 + 大仓位
- 🟡 **观察/不加仓**：MACD 空头 或 白<黄线
- 🟢 **趋势持有**：MACD 多头 + 白>黄
- ⚠️ **现金警戒**：现金 < 10% 时提示风险

Result：生成每只持仓股的操作建议文字。

---

### Step 6 — 更新持仓总览看板 — CONFIRM

文件路径：`持仓/仓位总览.md`

表格列：`股票 | 代码 | 成本 | 现价(M/D) | 仓位 | 盈亏 | MACD(5,34,5)`

MACD 列写：`金叉` / `死叉` / `多头` / `空头`（`死叉` 触发 Web 红色警告）

操作要点格式：
```markdown
## 本周操作要点

### 1. [标题]
| 股票 | 动作 | 条件 | 目标仓位 |

### 2. [标题]
- 文字描述
```

> CONFIRM：写入前展示新内容摘要，确认后执行。

Result：`持仓/仓位总览.md` 更新完毕。

---

### Step 7 — 重启 Web 服务并验证

```powershell
$p = (Get-NetTCPConnection -LocalPort 8002 -State Listen -ErrorAction SilentlyContinue).OwningProcess
if ($p) { taskkill /PID $p /F }
python -m uvicorn server.app:app --host 127.0.0.1 --port 8002
```

验证：访问 `http://127.0.0.1:8002/` 返回 HTTP 200。

Result：Web 服务正常运行，本次更新流程全部完成。

## Outputs

- `dailyOperations.txt`：新增一条含【资金信息】【持仓状态】【今日操作】的日期记录
- `持仓/仓位总览.md`：更新持仓表格 + 本周操作要点
- 操作建议文字（展示给用户，含 🔴🟡🟢⚠️ 分级）
- Web 服务 `http://127.0.0.1:8002/` 重启成功

## Error handling / Fallback

- **截图字段缺失或模糊**：逐字段询问用户，禁止推测数值
- **update_daily_ops.py 报错**：打印完整错误信息，检查 `--holdings` JSON 格式与字段完整性
- **回测脚本网络超时**：设置 `os.environ['no_proxy'] = '*'` 后重试；仍失败则跳过该股并标注
- **MACD 数据拉取失败**：跳过信号分析，在建议中注明"数据获取失败，信号待确认"
- **端口 8002 无法释放**：提示用户手动关闭进程，再重试 Step 7
- **日期已存在于 dailyOperations.txt**：提示用户确认是否覆盖，默认不覆盖 — CONFIRM

## Resources

- `scripts/update_daily_ops.py` — 解析持仓 JSON，对比上日仓位推算今日操作，追加记录到 `dailyOperations.txt`
