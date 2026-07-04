import requests
from config import BINANCE_API


def get_crypto(symbol: str):
    """
    Отримує поточну інформацію про монету:
    - ціна
    - зміна за 24 години
    - максимум
    - мінімум
    - об'єм
    """

    url = BINANCE_API + f"ticker/24hr?symbol={symbol}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        return {
            "price": float(data["lastPrice"]),
            "change": float(data["priceChangePercent"]),
            "high": float(data["highPrice"]),
            "low": float(data["lowPrice"]),
            "volume": float(data["volume"]),
        }

    except Exception as e:
        print(f"Помилка Binance: {e}")
        return None


def get_klines(symbol: str, interval="1h", limit=200):
    """
    Отримує історію свічок Binance.
    Потрібно для RSI, EMA, MACD та AI-аналізу.
    """

    url = BINANCE_API + (
        f"klines?symbol={symbol}&interval={interval}&limit={limit}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()

    except Exception as e:
        print(f"Помилка отримання свічок: {e}")
        return None