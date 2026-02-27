# execution/execution_router.py

import random


class ExecutionRouter:
    """
    Pure execution worker.
    Does ONE cycle.
    Orchestrator owns loops and session control.
    """

    def __init__(self, state, tracker, risk, intel, confluence):
        self.state = state
        self.tracker = tracker
        self.risk = risk
        self.intel = intel
        self.confluence = confluence

        self.cycles_completed = 0

    def run_cycle(self):
        """
        Executes ONE decision cycle.
        Returns structured result to Orchestrator.
        """

        if self.state.mode == "HALTED":
            return {"status": "HALTED"}

        snapshot = self.intel.generate_snapshot()

        score, threshold, decision = self.confluence.calculate(snapshot)

        result = {
            "snapshot": snapshot,
            "score": score,
            "threshold": threshold,
            "decision": decision,
            "trade_executed": False,
            "trade_return": 0.0,
            "equity": self.state.equity,
            "drawdown": self.state.total_drawdown_pct,
            "mode": self.state.mode,
        }

        if decision == "FILTER":
            self.cycles_completed += 1
            return result
        
        print("Router Execute Called")

        # Trade execution
        if self.state.mode == "DEFENSIVE":
            trade_return = random.uniform(-1, 1)
        else:
            trade_return = random.uniform(-2, 2)

        self.tracker.update_equity(self.state, trade_return)
        risk_status = self.risk.evaluate(self.state)

        self.cycles_completed += 1

        result.update({
            "trade_executed": True,
            "trade_return": trade_return,
            "equity": self.state.equity,
            "drawdown": self.state.total_drawdown_pct,
            "mode": self.state.mode,
            "risk_status": risk_status
        })

        return result

    async def execute(self):

        print("Router Execute Called")

        pnl = 0 #Always initiate first

        return {
            "executed": False,
            "pnl": 0,
            "reason": "UNKNOWN"
        }
        
        pnl = self.simulate_trade()

        result["executed"] = True
        result["pnl"] = pnl
        result["reason"] = "PERMIT"


        result["executed"] = False
        result["pnl"] = 0
        result["reason"] = "FILTER"

        return result

        