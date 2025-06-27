import logging
from telegram.ext import Updater, CommandHandler, CallbackContext
from services.telegram_service import TelegramBot
from config.settings import TIMEZONE
from utils.logger import setup_logging
import asyncio
import datetime

# Set up logging
logger = setup_logging()

def daily_predictions(context: CallbackContext):
    bot = TelegramBot()
    asyncio.run(bot.send_daily_predictions())

def weekend_preview(context: CallbackContext):
    bot = TelegramBot()
    asyncio.run(bot.send_weekend_preview())

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Schedule daily predictions at 9:00 AM
    updater.job_queue.run_daily(
        daily_predictions,
        time=datetime.time(hour=9, minute=0, tzinfo=TIMEZONE),
        days=(0, 1, 2, 3, 4, 5, 6)
    )

    # Schedule weekend preview on Friday at 17:00
    updater.job_queue.run_daily(
        weekend_preview,
        time=datetime.time(hour=17, minute=0, tzinfo=TIMEZONE),
        days=(4,)
    )

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
