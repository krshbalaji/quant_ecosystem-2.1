from config.profile import PROFILE
from execution.execution_router import ExecutionRouter
from kernel.system_state import SystemState
from kernel.equity_tracker import EquityTracker
from kernel.risk_controller import RiskController
from intelligence.market_intelligence import MarketIntelligence
from confluence.adaptive_confluence_engine import AdaptiveConfluenceEngine


def build_router():

    state = SystemState(PROFILE)
    tracker = EquityTracker()
    risk = RiskController()
    intel = MarketIntelligence()
    confluence = AdaptiveConfluenceEngine()

    state.reset_daily()

    router = ExecutionRouter(
        state=state,
        tracker=tracker,
        risk=risk,
        intel=intel,
        confluence=confluence
    )

    return router