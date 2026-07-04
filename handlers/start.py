from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Команда /start
    """

    text = (
        "👋 Вітаю!\n\n"
        "Я *Volodya AI Trader* 🤖\n\n"
        "Допоможу тобі:\n"
        "📈 Аналізувати крипторинок\n"
        "🤖 Отримувати AI-сигнали\n"
        "📰 Читати новини\n"
        "💼 Вести портфель\n"
        "🔔 Створювати алерти\n\n"
        "👇 Обери потрібний розділ."
    )

    await update.message.reply_text(
        text=text,
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )