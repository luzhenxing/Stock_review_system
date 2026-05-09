---
name: daily-backtest-update
description: >-
  每日持仓回测更新工作流。分析用户发送的持仓截图，自动更新 dailyOperations.txt（含【持仓状态】【今日操作】【资金信息】），对当前持仓跑无情操盘手回测，生成操作建议，更新持仓看板，重启 Web 服务。
  当用户说"帮我更新回测"、"更新持仓"、"回测一下"，或发送持仓截图时触发。
---

# 每日持仓回测更新

## 工作流（按顺序执行）

### Step 1 — 解析持仓截图

从用户提供的截图中提取以下字段：

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

### Step 2 — 运行 update_daily_ops.py

```bash
cd <PROJECT_ROOT>
python -X utf8 ".cursor/skills/daily-backtest-update/scripts/update_daily_ops.py" \
  --date "YYYY-MM-DD" \
  --total-assets <总资产> \
  --available-cash <余额> \
  --holdings '<JSON>'
```

`--holdings` JSON 格式：
```json
[
  {"code": "600487", "name": "亨通光电", "position_pct": 11.0, "cost": 56.45, "price": 77.27, "market_value": 77270},
  {"name": "现金", "position_pct": 0.4, "is_cash": true}
]
```

脚本会自动：
- 对比上一条记录推算【今日操作】
- 计算【资金信息】（总资产、可用、本金50万、盈亏、净值）
- 追加新日期条目到 `dailyOperations.txt`

### Step 3 — 跑无情操盘手回测（1年 + 2年）

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

### Step 4 — 拉取最新 MACD + 白黄线状态

```python
from fetch_wave_data import fetch_kline, calc_macd, calc_ema, calc_sma
# calc_dema(closes, 10) = 白线；calc_quad_ma(closes) = 黄线
# 判断：金叉/死叉/多头/空头；白>黄 / 白<黄
```

### Step 5 — 生成操作建议

基于回测结果 + 当前信号，按优先级给出：

- 🔴 **减仓**：白<黄线 + 2年回测负收益 + 大仓位
- 🟡 **观察/不加仓**：MACD空头 或 白<黄线
- 🟢 **趋势持有**：MACD多头 + 白>黄
- ⚠️ **现金警戒**：现金 < 10% 时提示风险

### Step 6 — 更新 持仓/仓位总览.md

文件路径：`持仓/仓位总览.md`

表格列：`股票 | 代码 | 成本 | 现价(M/D) | 仓位 | 盈亏 | MACD(5,34,5)`

MACD列内容：`金叉` / `死叉` / `多头` / `空头`（`死叉`会触发 Web 红色警告）

操作要点部分格式：
```markdown
## 本周操作要点

### 1. [标题]
| 股票 | 动作 | 条件 | 目标仓位 |

### 2. [标题]
- 文字描述
```

### Step 7 — 重启 Web 服务

```powershell
$p = (Get-NetTCPConnection -LocalPort 8002 -State Listen -ErrorAction SilentlyContinue).OwningProcess
if ($p) { taskkill /PID $p /F }
python -m uvicorn server.app:app --host 127.0.0.1 --port 8002
```

验证：访问 `http://127.0.0.1:8002/` 返回 HTTP 200。

---

## 项目固定信息

| 项目 | 值 |
|------|-----|
| 本金 | ¥500,000 |
| Web 端口 | 8002 |
| 持仓总览 | `持仓/仓位总览.md` |
| 日志文件 | `dailyOperations.txt` |
| 回测脚本 | `脚本/backtest_ruthless.py` |
| 工具脚本 | `.cursor/skills/daily-backtest-update/scripts/update_daily_ops.py` |

## 注意事项

- 科创板（688 开头）股票 fetch_kline 可正常拉取
- 运行 Python 时加 `-X utf8` 避免 Windows 中文编码问题
- 重启 uvicorn 前先确认端口占用进程
