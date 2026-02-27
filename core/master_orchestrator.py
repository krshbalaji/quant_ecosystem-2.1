import datetime
import asyncio
from core.logger import SystemLogger

class MasterOrchestrator:
    """
    Supreme control layer of QE-2.1
    Owns:
    - Session loop
    - Time phases
    - Global circuit breaker
    """

    def __init__(self):
        self.global_max_drawdown = 8.0  # percent
        self.session_active = True
        self.fast_mode = True
        self.logger = SystemLogger()
        self.consecutive_losses = 0
        self.verbose = False

                    
    def get_phase(self):
        if self.fast_mode:
            return "ACTIVE_MARKET"
        

        now = datetime.datetime.now().time()

        if now < datetime.time(8, 30):
            return "MAINTENANCE"
        elif now < datetime.time(9, 0):
            return "GLOBAL_SCAN"
        elif now < datetime.time(9, 15):
            return "RHYTHM_SCAN"
        elif now < datetime.time(15, 30):
            return "ACTIVE_MARKET"
        else:
            return "POST_MARKET"

    async def start(self, router):

        cycle = 0

        while True:
            cycle += 1

            phase = self.get_phase()

            print(f"Cycle: {cycle} | Phase: {phase}")

            if phase != "ACTIVE_MARKET":
                await asyncio.sleep(1)
                continue

            result = await router.execute()

            if self.fast_mode and cycle >= 30:
                print("🧪 Fast mode cycle limit reached")
                break
            result = await router.execute()

            if result["executed"]:
                print(f"Cycle {cycle} → Executed | PnL: {result['pnl']}")
            else:
                print(f"Cycle {cycle} → Skipped | Reason: {result['reason']}")    
            
            await asyncio.sleep(0.2)

        print("\n🏁 Session Controlled by Orchestrator Complete")