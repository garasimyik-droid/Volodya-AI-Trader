from telegram import Update
from telegram.ext import ContextTypes

from analysis import ai_analysis


async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    AI аналіз Bitcoin
    """

    result = ai_analysis("BTCUSDT")

    if result is None:

        await update.message.reply_text(
            "❌ Не вдалося виконати аналіз."
        )

        return

    message = f"""
🤖 AI Аналіз

🪙 BTCUSDT

━━━━━━━━━━━━━━━━━━

💰 Ціна
{result["price"]}

📈 Тренд
{result["trend"]}

📊 RSI
{result["rsi"]}

📉 EMA20
{result["ema20"]}

📉 EMA50
{result["ema50"]}

📉 EMA200
{result["ema200"]}

⚡ MACD
{result["macd"]}

🟢 Сигнал
{result["signal"]}

🎯 Ймовірність
{result["probability"]}%

🛡 Підтримка
{result["support"]}

🚀 Опір
{result["resistance"]}
"""

    await update.message.reply_text(message)