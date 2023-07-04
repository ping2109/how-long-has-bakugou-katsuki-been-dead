import datetime
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def date():
    current_date = datetime.datetime.now().date()

    target_date = datetime.date(2022, 8, 1)

    days_since = (current_date - target_date).days

    text=f"It has been {days_since} days since Bakugou Katsuki died."
    return text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=date())

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
