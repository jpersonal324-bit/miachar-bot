import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "8781692817:AAG0mlcujZUI54IbWmoIr9KRlnUYX0BwKgE")

usuarios_vistos = set()

MENSAJE_BIENVENIDA = (
      "Hola bb\n\n"
      "Videollamada:\n"
      "45 dolares 20 minutos\n"
      "30 dolares 10 minutos\n\n"
      "30 dolares 10 videos\n\n"
      "Acepto: PayPal, Zelle y Remitly"
)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
      user_id = update.effective_user.id
      if user_id not in usuarios_vistos:
                usuarios_vistos.add(user_id)
                await update.message.reply_text(MENSAJE_BIENVENIDA)

  if __name__ == "__main__":
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.PRIVATE, responder))
        print("Bot corriendo...")
        app.run_polling()
