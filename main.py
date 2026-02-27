import asyncio
from config.profile import PROFILE
from kernel.system_state import SystemState
from kernel.equity_tracker import EquityTracker
from kernel.risk_controller import RiskController
from intelligence.market_intelligence import MarketIntelligence
from confluence.adaptive_confluence_engine import AdaptiveConfluenceEngine
from execution.execution_router import ExecutionRouter
from core.master_orchestrator import MasterOrchestrator


async def main():
    
    print("🔥 Quant Ecosystem 2.1 Booting...")

    orchestrator = MasterOrchestrator()

    state = SystemState(PROFILE)
    tracker = EquityTracker()
    risk = RiskController()
    intel = MarketIntelligence()
    confluence = AdaptiveConfluenceEngine()

    state.reset_daily()

    router = ExecutionRouter(state, tracker, risk, intel, confluence)

    # --- Master Brain ---
    orchestrator = MasterOrchestrator()

    await orchestrator.start(router)


if __name__ == "__main__":
    asyncio.run(main())
