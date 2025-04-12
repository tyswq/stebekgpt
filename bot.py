import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]  # Токен из переменных окружения

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я - стебекгпт ебланская нейросеть могу ответить либо дилдо либо пенис по моему выбору а теперь иди нахуй!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = random.choice(["дилдо", "пенис"])
    await update.message.reply_text(response)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
