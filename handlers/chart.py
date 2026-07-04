from telegram import Update
from telegram.ext import ContextTypes


async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Аналіз графіка (заготовка)
    """

    text = (
        "📷 Аналіз графіка\n\n"
        "Надішли мені скріншот із TradingView.\n\n"
        "У наступній версії я автоматично визначатиму:\n\n"
        "📈 Тренд\n"
        "📊 RSI\n"
        "📉 EMA\n"
        "⚡ MACD\n"
        "🎯 Support\n"
        "🚀 Resistance\n"
        "💧 Liquidity\n"
        "📦 Order Blocks\n"
        "🔥 Fair Value Gap\n"
        "🟢 LONG / 🔴 SHORT\n"
    )

    await update.message.reply_text(text)