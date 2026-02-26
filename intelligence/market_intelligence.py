# intelligence/market_intelligence.py

import random


class MarketIntelligence:

    def generate_snapshot(self):
        bias = random.choice(["BULLISH", "BEARISH", "NEUTRAL"])
        volatility_state = random.choice(["LOW", "NORMAL", "HIGH"])
        regime = random.choice(["TREND", "RANGE", "COMPRESSION"])

        volatility_ratio = round(random.uniform(0.3, 0.9), 2)

        return {
            "bias": bias,
            "volatility_state": volatility_state,
            "volatility_ratio": volatility_ratio,
            "regime": regime
        }