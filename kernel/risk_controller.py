# kernel/risk_controller.py

class RiskController:
    def evaluate(self, state):
        # Daily loss check
        if state.daily_pnl <= -state.daily_max_loss_pct:
            state.mode = "HALTED"
            return "Daily loss limit breached"

        # Total drawdown check
        if state.total_drawdown_pct >= state.max_drawdown_pct:
            state.mode = "HALTED"
            return "Maximum drawdown breached"

        # Defensive trigger (half of max drawdown)
        if state.total_drawdown_pct >= state.max_drawdown_pct / 2:
            state.mode = "DEFENSIVE"
            return "Switching to defensive mode"

        state.mode = "ACTIVE"
        return "Operating normally"