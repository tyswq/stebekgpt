import os
import random
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Веб-сервер Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот в порядке! Пинг успешен."

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Список brainrot-фраз
BRAINROT_PHRASES = [
    "tralalelo tralala",
    "trippi troppa troppa trippa",
    "bombordiro crocodilo",
    "lirili larila",
    "brr brr patapin"
]

async def brainrot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /brainrot"""
    response = random.choice(BRAINROT_PHRASES)
    await update.message.reply_text(response)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я - стебекгпт ебланская нейросеть могу ответить либо дилдо либо пенис по моему выбору а теперь иди нахуй!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик обычных сообщений"""
    user_text = update.message.text.lower()
    
    # Специальные ответы
    if user_text in ["кто долбоеб?", "кто хуесос?"]:
        await update.message.reply_text("макан")
    elif user_text in ["кто фембойчик", "кто фембойчик?"]:
        await update.message.reply_text("Никита")
    else:
        # 1% шанс на особый ответ
        if random.random() < 0.01:
            await update.message.reply_text("я знаю где ты живешь ебаный пидорас я нашлю на тебя роботов-пидоров")
        else:
            # Стандартный рандомный ответ
            response = random.choice(["дилдо", "пенис"])
            await update.message.reply_text(response)

def run_bot():
    while True:
        try:
            application = Application.builder().token(os.environ['BOT_TOKEN']).build()
            
            # Добавляем все обработчики
            application.add_handler(CommandHandler("start", start))
            application.add_handler(CommandHandler("brainrot", brainrot))
            application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
            
            logger.info("Бот запущен!")
            application.run_polling()
            
        except Exception as e:
            logger.error(f"Ошибка: {e}. Перезапуск через 5 секунд...")
            time.sleep(5)

if __name__ == '__main__':
    Thread(target=run_flask, daemon=True).start()
    run_bot()
