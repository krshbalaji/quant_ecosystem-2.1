# kernel/system_state.py

class SystemState:
    def __init__(self, profile):
        self.capital_base = profile["capital_base"]
        self.daily_max_loss_pct = profile["daily_max_loss_pct"]
        self.max_drawdown_pct = profile["max_drawdown_pct"]
        self.growth_mode = profile["growth_mode"]

        self.equity = self.capital_base
        self.peak_equity = self.capital_base

        self.daily_pnl = 0
        self.total_drawdown_pct = 0

        self.mode = "INIT"  # INIT / ACTIVE / DEFENSIVE / HALTED

    def reset_daily(self):
        self.daily_pnl = 0
        self.mode = "ACTIVE"