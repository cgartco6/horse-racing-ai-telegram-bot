from telegram import Bot, ParseMode
from config.settings import CHANNEL_ID, TELEGRAM_TOKEN
from services.prediction_engine import PredictionEngine
from utils.formatters import format_race_time
import asyncio

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_TOKEN)
        self.engine = PredictionEngine()
        
    async def send_daily_predictions(self):
        races = self.engine.generate_daily_races()
        message = self._format_message(races)
        await self.bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    def _format_message(self, races):
        msg = "🏇 *AI HORSE RACING PREDICTIONS* 🏁\n\n"
        for track, race_list in races.items():
            msg += f"🏟️ *{track.upper()}*\n"
            for race in race_list:
                # Predict the race
                race = self.engine.predict_race(race)
                top_pick = race['predictions'][0]
                msg += f"⏱️ {race['time']} | {race['distance']}m | {race['going']}\n"
                msg += f"⭐ *Top Pick*: {top_pick['horse']} ({top_pick['ai_win_prob']*100:.1f}%)\n"
                msg += f"  Jockey: {top_pick['jockey']} ({top_pick['jockey_win_rate']*100:.1f}%) | Weight: {top_pick['weight']}kg\n"
                msg += f"  Trainer: {top_pick['trainer']} | Age: {top_pick['horse_age']}\n"
                msg += f"  *Bookies*: HW {top_pick['hollywoodbets']*100:.1f}% | BW {top_pick['betway']*100:.1f}%\n\n"
        msg += "⚠️ _Predictions are probabilistic and for informational purposes only_"
        return msg

    async def send_weekend_preview(self):
        # Weekend prediction logic (similar but for Saturday and Sunday)
        pass
