# bot/handlers.py
from telegram import Update
from telegram.ext import ContextTypes
from .weather_service import get_weather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde al comando /start."""
    await update.message.reply_text(
        "¡Hola! Soy tu Bot del Clima. Dime el nombre de una ciudad y te diré cómo está el tiempo allí."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde al comando /help."""
    await update.message.reply_text("Solo tienes que escribirme el nombre de una ciudad (ej: Madrid).")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa cualquier mensaje de texto que no sea un comando."""
    city = update.message.text
    response = get_weather(city)
    await update.message.reply_text(response)
