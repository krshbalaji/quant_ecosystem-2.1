# execution/execution_router.py

import random


class ExecutionRouter:

    def __init__(self, state, tracker, risk, intel, confluence):
        self.state = state
        self.tracker = tracker
        self.risk = risk
        self.intel = intel
        self.confluence = confluence

    def run_session(self, cycles=5):
        print("\n🚦 Starting Execution Session")

        for cycle in range(cycles):

            if self.state.mode == "HALTED":
                print("🛑 System Halted. Ending Session.")
                break

            snapshot = self.intel.generate_snapshot()

            print("\n📊 Intelligence Snapshot")
            print(snapshot)

            score, threshold, decision = self.confluence.calculate(snapshot)

            print(f"Confluence Score: {score}")
            print(f"Threshold: {threshold}")
            print(f"Decision: {decision}")

            if decision == "FILTER":
                print("🚫 Trade Blocked")
                continue

            if self.state.mode == "DEFENSIVE":
                trade_return = random.uniform(-1, 1)  # reduced volatility
            else:
                trade_return = random.uniform(-2, 2)

            print(f"\n⚡ Executing Trade: {trade_return:.2f}%")

            self.tracker.update_equity(self.state, trade_return)
            status = self.risk.evaluate(self.state)

            print(f"Equity: ₹{self.state.equity:,.2f}")
            print(f"Drawdown: {self.state.total_drawdown_pct:.2f}%")
            print(f"Mode: {self.state.mode}")
            print(f"Risk Status: {status}")

        print("\n✅ Session Complete")

    
    def run_continuous(self, sleep_interval=1, max_cycles=100):

        import time
        import random

        print("\n🧠 Autonomous Engine Activated (Fast Mode)")

        cycle_count = 0

        while cycle_count < max_cycles:

            if self.state.mode == "HALTED":
                print("🛑 System Halted. Awaiting Manual Intervention.")
                break

            cycle_count += 1
            print(f"\n🔄 Cycle {cycle_count}")

            # Placeholder: future health check hook
            # self.health_monitor.check()

            snapshot = self.intel.generate_snapshot()
            print("📊 Snapshot:", snapshot)

            score, threshold, decision = self.confluence.calculate(snapshot)

            print(f"Score: {score} | Threshold: {threshold} | Decision: {decision}")

            if decision == "PERMIT":

                if self.state.mode == "DEFENSIVE":
                    trade_return = random.uniform(-1, 1)
                else:
                    trade_return = random.uniform(-2, 2)

                print(f"⚡ Executing Trade: {trade_return:.2f}%")

                self.tracker.update_equity(self.state, trade_return)
                status = self.risk.evaluate(self.state)

                print(f"Equity: ₹{self.state.equity:,.2f}")
                print(f"Drawdown: {self.state.total_drawdown_pct:.2f}%")
                print(f"Mode: {self.state.mode}")
                print(f"Risk: {status}")

            else:
                print("🚫 Trade Skipped")

            time.sleep(sleep_interval)

        print("\n✅ Autonomous Session Completed")