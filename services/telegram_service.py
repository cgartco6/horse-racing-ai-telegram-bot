from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
from services.prediction_engine import PredictionEngine
from config.settings import CHANNEL_ID

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_TOKEN)
        self.engine = PredictionEngine()
        
    def send_daily_predictions(self):
        races = self.engine.generate_daily_races()
        message = self._format_message(races)
        self.bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    def _format_message(self, races):
        msg = "🏇 *AI HORSE RACING PREDICTIONS* 🏁\n\n"
        for track, races in races.items():
            msg += f"🏟️ *{track.upper()}*\n"
            for race in races:
                msg += f"⏱️ {race['time']} | {race['distance']}m\n"
                msg += f"⭐ TOP PICK: {race['top_pick']['name']} ({race['top_pick']['prob']}%)\n"
                msg += f"  Jockey: {race['top_pick']['jockey']} | Weight: {race['top_pick']['weight']}kg\n\n"
        return msg

    def send_weekend_preview(self):
        # Weekend prediction logic
        pass
