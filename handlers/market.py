from telegram import Update
from telegram.ext import ContextTypes

from config import COINS
from crypto import get_crypto
from keyboards import market_menu, main_menu


async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Відкрити меню ринку
    """

    await update.message.reply_text(
        "📈 Оберіть криптовалюту:",
        reply_markup=market_menu()
    )


async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Відображення інформації про монету
    """

    text = update.message.text

    coin_name = text.replace("₿ ", "") \
                    .replace("⚡ ", "") \
                    .replace("💎 ", "") \
                    .replace("☀️ ", "") \
                    .replace("🟡 ", "") \
                    .replace("🐶 ", "") \
                    .replace("🐸 ", "") \
                    .replace("🌍 ", "") \
                    .replace("🟢 ", "")

    if coin_name not in COINS:
        return

    coin = COINS[coin_name]

    data = get_crypto(coin["symbol"])

    if data is None:

        await update.message.reply_text(
            "❌ Не вдалося отримати дані Binance."
        )

        return

    trend = "🟢 LONG" if data["change"] >= 0 else "🔴 SHORT"

    message = f"""
{coin['emoji']} {coin['name']}

💰 Ціна:
{data['price']:.4f} USDT

📊 Зміна 24h:
{data['change']:.2f}%

📈 Максимум:
{data['high']:.4f}

📉 Мінімум:
{data['low']:.4f}

📦 Обсяг:
{data['volume']:,.0f}

📍 Сигнал:
{trend}
"""

    await update.message.reply_text(message)


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🏠 Головне меню",
        reply_markup=main_menu()
    )