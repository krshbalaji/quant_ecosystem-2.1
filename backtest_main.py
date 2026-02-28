import asyncio
from core.system_factory import build_router
from research.backtest_engine import BacktestEngine


async def main():

    router = build_router()

    engine = BacktestEngine(router, cycles=10000)

    report = await engine.run()

    print("\n📊 BACKTEST REPORT")
    print("-" * 40)

    for k, v in report.items():
        print(f"{k:<20}: {v}")

    engine.export_equity_curve()


if __name__ == "__main__":
    asyncio.run(main())
