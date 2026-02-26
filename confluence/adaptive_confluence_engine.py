# confluence/adaptive_confluence_engine.py


class AdaptiveConfluenceEngine:

    def calculate(self, snapshot):
        score = 0

        if snapshot["bias"] == "BULLISH":
            score += 25
        elif snapshot["bias"] == "BEARISH":
            score += 20
        else:
            score += 10

        if snapshot["volatility_state"] == "HIGH":
            score += 20
        elif snapshot["volatility_state"] == "NORMAL":
            score += 15
        else:
            score += 5

        if snapshot["regime"] == "TREND":
            score += 25
        elif snapshot["regime"] == "RANGE":
            score += 15
        else:
            score += 10

        score += snapshot["volatility_ratio"] * 20

        threshold = 60

        decision = "PERMIT" if score >= threshold else "FILTER"

        return round(score, 2), threshold, decision