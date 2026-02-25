from config.profile import PROFILE
from kernel.system_state import SystemState
from kernel.equity_tracker import EquityTracker
from kernel.risk_controller import RiskController
import random


def main():
    print("🔥 Quant Ecosystem 2.1 Booting...")

    state = SystemState(PROFILE)
    tracker = EquityTracker()
    risk = RiskController()

    state.reset_daily()

    print(f"Capital Base: ₹{state.capital_base}")
    print("System Mode:", state.mode)

    # Simulated test trades
    for i in range(5):
        trade_return = random.uniform(-2, 2)  # simulate %
        pnl = tracker.update_equity(state, trade_return)
        status = risk.evaluate(state)

        print(f"\nTrade {i+1}: {trade_return:.2f}%")
        print(f"Equity: ₹{state.equity:,.2f}")
        print(f"Drawdown: {state.total_drawdown_pct:.2f}%")
        print(f"Mode: {state.mode}")
        print(f"Risk Status: {status}")

        if state.mode == "HALTED":
            print("🛑 Trading Halted")
            break

    print("\n✅ Kernel Test Complete")


if __name__ == "__main__":
    main()