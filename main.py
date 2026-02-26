from config.profile import PROFILE
from kernel.system_state import SystemState
from kernel.equity_tracker import EquityTracker
from kernel.risk_controller import RiskController
from intelligence.market_intelligence import MarketIntelligence
from confluence.adaptive_confluence_engine import AdaptiveConfluenceEngine
from execution.execution_router import ExecutionRouter


def main():
    print("🔥 Quant Ecosystem 2.1 Booting...")

    state = SystemState(PROFILE)
    tracker = EquityTracker()
    risk = RiskController()
    intel = MarketIntelligence()
    confluence = AdaptiveConfluenceEngine()

    state.reset_daily()

    router = ExecutionRouter(state, tracker, risk, intel, confluence)

    router.run_continuous(sleep_interval=1, max_cycles=30)


if __name__ == "__main__":
    main()