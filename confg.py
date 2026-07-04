import os
from dotenv import load_dotenv

# Завантаження змінних середовища
load_dotenv()

# Telegram Bot Token
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Binance API
BINANCE_API = "https://api.binance.com/api/v3/"

# Таймфрейми
TIMEFRAMES = {
    "15m": "15m",
    "1h": "1h",
    "4h": "4h",
    "1d": "1d"
}

# Список монет
COINS = {
    "BTC": {
        "symbol": "BTCUSDT",
        "emoji": "📈",
        "name": "Bitcoin"
    },
    "ETH": {
        "symbol": "ETHUSDT",
        "emoji": "⚡",
        "name": "Ethereum"
    },
    "XRP": {
        "symbol": "XRPUSDT",
        "emoji": "💎",
        "name": "XRP"
    },
    "SOL": {
        "symbol": "SOLUSDT",
        "emoji": "☀️",
        "name": "Solana"
    },
    "BNB": {
        "symbol": "BNBUSDT",
        "emoji": "🟡",
        "name": "BNB"
    },
    "DOGE": {
        "symbol": "DOGEUSDT",
        "emoji": "🐶",
        "name": "Dogecoin"
    }
}