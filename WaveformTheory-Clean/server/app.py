"""
波浪交易看板 — 独立服务

启动: uvicorn server.app:app --host 127.0.0.1 --port 8002
"""

import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from jinja2 import Environment, FileSystemLoader

from server.wave_parser import (
    parse_holdings, parse_action_items, parse_daily_logs,
    load_backtest, get_update_date,
)

app = FastAPI(title="波浪交易看板")

_template_dir = os.path.join(os.path.dirname(__file__), "templates")
_jinja_env = Environment(loader=FileSystemLoader(_template_dir), autoescape=True)


@app.get("/", response_class=HTMLResponse)
@app.get("/stock_dashboard", response_class=HTMLResponse)
def stock_dashboard():
    """波浪交易看板"""
    holdings = parse_holdings()
    actions = parse_action_items()
    logs = parse_daily_logs(days=7)
    backtest = load_backtest()
    update_date = get_update_date()

    cash_h = [h for h in holdings if h["is_cash"]]
    cash_pct = cash_h[0]["position"] if cash_h else "?"
    cash_value = _parse_pct(cash_pct)
    cash_alert_level = None
    if cash_value < 15:
        cash_alert_level = "danger"
    elif cash_value < 30:
        cash_alert_level = "warning"

    death_stocks = [h["name"] for h in holdings if h["is_death"]]

    template = _jinja_env.get_template("wave.html")
    return HTMLResponse(template.render(
        holdings=holdings,
        actions=actions,
        logs=logs,
        backtest=backtest,
        update_date=update_date,
        cash_pct=cash_pct,
        cash_alert_level=cash_alert_level,
        death_stocks=death_stocks,
    ))


def _parse_pct(text: str) -> float:
    digits = "".join(ch for ch in text if ch.isdigit() or ch == ".")
    return float(digits) if digits else 0.0
