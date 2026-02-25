# kernel/equity_tracker.py

class EquityTracker:
    def update_equity(self, state, trade_return_pct):
        pnl_amount = state.equity * (trade_return_pct / 100)
        state.equity += pnl_amount
        state.daily_pnl += trade_return_pct

        if state.equity > state.peak_equity:
            state.peak_equity = state.equity

        drawdown = (
            (state.peak_equity - state.equity)
            / state.peak_equity
        ) * 100

        state.total_drawdown_pct = drawdown

        return pnl_amount