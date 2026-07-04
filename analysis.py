import pandas as pd
import ta

from crypto import get_klines


class MarketAnalysis:

    def __init__(self, symbol, interval="1h"):

        self.symbol = symbol
        self.interval = interval

        self.df = None

    def load_data(self):

        candles = get_klines(
            self.symbol,
            self.interval,
            limit=250
        )

        if candles is None:
            return False

        self.df = pd.DataFrame(candles)

        self.df = self.df.iloc[:, :6]

        self.df.columns = [
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]

        self.df["open"] = self.df["open"].astype(float)
        self.df["high"] = self.df["high"].astype(float)
        self.df["low"] = self.df["low"].astype(float)
        self.df["close"] = self.df["close"].astype(float)
        self.df["volume"] = self.df["volume"].astype(float)

        return True

    def calculate_indicators(self):

        close = self.df["close"]

        self.df["EMA20"] = ta.trend.ema_indicator(
            close,
            window=20
        )

        self.df["EMA50"] = ta.trend.ema_indicator(
            close,
            window=50
        )

        self.df["EMA200"] = ta.trend.ema_indicator(
            close,
            window=200
        )

        self.df["RSI"] = ta.momentum.rsi(
            close,
            window=14
        )

        macd = ta.trend.MACD(close)

        self.df["MACD"] = macd.macd()

        self.df["MACD_SIGNAL"] = macd.macd_signal()

        self.df["MACD_DIFF"] = macd.macd_diff()
            def get_support(self):

        return round(
            self.df["low"].tail(30).min(),
            4
        )

    def get_resistance(self):

        return round(
            self.df["high"].tail(30).max(),
            4
        )

    def get_trend(self):

        last = self.df.iloc[-1]

        if (
            last["EMA20"] >
            last["EMA50"] >
            last["EMA200"]
        ):
            return "🟢 Bullish"

        if (
            last["EMA20"] <
            last["EMA50"] <
            last["EMA200"]
        ):
            return "🔴 Bearish"

        return "🟡 Sideways"

    def get_signal(self):

        last = self.df.iloc[-1]

        if (
            last["RSI"] < 35
            and last["MACD"] > last["MACD_SIGNAL"]
        ):
            return "🟢 LONG"

        if (
            last["RSI"] > 65
            and last["MACD"] < last["MACD_SIGNAL"]
        ):
            return "🔴 SHORT"

        return "🟡 WAIT"

    def get_probability(self):

        score = 50

        last = self.df.iloc[-1]

        if last["EMA20"] > last["EMA50"]:
            score += 10

        if last["EMA50"] > last["EMA200"]:
            score += 10

        if last["MACD"] > last["MACD_SIGNAL"]:
            score += 10

        if 45 <= last["RSI"] <= 60:
            score += 10

        if score > 90:
            score = 90

        if score < 10:
            score = 10

        return score
            def analyze(self):

        if not self.load_data():
            return None

        self.calculate_indicators()

        last = self.df.iloc[-1]

        return {

            "price": round(last["close"], 4),

            "trend": self.get_trend(),

            "signal": self.get_signal(),

            "probability": self.get_probability(),

            "support": self.get_support(),

            "resistance": self.get_resistance(),

            "rsi": round(last["RSI"], 2),

            "ema20": round(last["EMA20"], 4),

            "ema50": round(last["EMA50"], 4),

            "ema200": round(last["EMA200"], 4),

            "macd": round(last["MACD"], 4),

            "macd_signal": round(last["MACD_SIGNAL"], 4),

            "macd_histogram": round(last["MACD_DIFF"], 4)

        }


def ai_analysis(symbol, interval="1h"):

    market = MarketAnalysis(symbol, interval)

    return market.analyze()