from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN

# Comando /start
async def start(update: Update, context):
    await update.message.reply_text("¡Hola! Soy un Echo Bot. Envíame un mensaje y te lo repetiré.")

# Función principal
def main():
    # Crear la aplicación
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Agregar manejadores
    application.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()


