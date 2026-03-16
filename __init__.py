# main.py
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.handlers import start, help_command, handle_message

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    
    if not token:
        print("Error: No se ha encontrado el TELEGRAM_TOKEN en el archivo .env")
        return

    # Construimos la aplicación del bot
    app = ApplicationBuilder().token(token).build()

    # Añadimos los manejadores de comandos y mensajes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot en marcha... Presiona Ctrl+C para detenerlo.")
    app.run_polling()

if __name__ == '__main__':
    main()
