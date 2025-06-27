import logging
from telegram.ext import Updater
from services.telegram_service import TelegramBot
from config.settings import TIMEZONE
from utils.logger import setup_logging

def main():
    setup_logging()
    tb = TelegramBot()
    
    updater = Updater(token=TELEGRAM_TOKEN)
    jq = updater.job_queue
    
    # Daily predictions at 9:00 AM
    jq.run_daily(
        lambda ctx: tb.send_daily_predictions(),
        time=datetime.time(9, 0, 0, tzinfo=TIMEZONE),
        days=(0, 1, 2, 3, 4, 5, 6)
    )
    
    # Weekend preview on Fridays
    jq.run_daily(
        lambda ctx: tb.send_weekend_preview(),
        time=datetime.time(17, 0, 0, tzinfo=TIMEZONE),
        days=(4,)
    )
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
