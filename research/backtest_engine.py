import csv
from statistics import mean



class BacktestEngine:

    def __init__(self, router, cycles=10000, starting_equity=100.0):
        self.router = router
        self.cycles = cycles
        self.starting_equity = starting_equity

        self.equity = starting_equity
        self.equity_peak = starting_equity

        self.trades = []
        self.drawdowns = []

    # --------------------------------------------------
    # Core Runner
    # --------------------------------------------------
    async def run(self):

        for i in range(self.cycles):

            result = await self.router.execute()

            if result.get("executed", False):

                pnl = float(result.get("pnl", 0.0))

                self.trades.append(pnl)

                self.equity *= (1 + pnl / 100)

                if self.equity > self.equity_peak:
                    self.equity_peak = self.equity

                dd = (
                    (self.equity_peak - self.equity)
                    / self.equity_peak
                ) * 100

                self.drawdowns.append(dd)

        return self.generate_report()

    # --------------------------------------------------
    # Analytics
    # --------------------------------------------------
    def generate_report(self):

        if not self.trades:
            return {"error": "No trades executed."}

        wins = [t for t in self.trades if t > 0]
        losses = [t for t in self.trades if t < 0]

        win_rate = len(wins) / len(self.trades) * 100
        avg_win = mean(wins) if wins else 0
        avg_loss = mean(losses) if losses else 0

        expectancy = (
            (win_rate / 100) * avg_win +
            ((100 - win_rate) / 100) * avg_loss
        )

        max_dd = max(self.drawdowns) if self.drawdowns else 0

        return {
            "Total Trades": len(self.trades),
            "Win Rate %": round(win_rate, 2),
            "Avg Win %": round(avg_win, 2),
            "Avg Loss %": round(avg_loss, 2),
            "Expectancy %": round(expectancy, 4),
            "Max Drawdown %": round(max_dd, 2),
            "Final Equity": round(self.equity, 2)
        }

    # --------------------------------------------------
    # Export CSV
    # --------------------------------------------------
    def export_equity_curve(self, filename="equity_curve.csv"):

        equity = self.starting_equity
        equity_peak = equity

        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Trade#", "PnL%", "Equity", "Drawdown%"])

            for i, pnl in enumerate(self.trades, start=1):

                equity *= (1 + pnl / 100)

                if equity > equity_peak:
                    equity_peak = equity

                dd = (
                    (equity_peak - equity)
                    / equity_peak
                ) * 100

                writer.writerow([i, pnl, round(equity, 4), round(dd, 4)])