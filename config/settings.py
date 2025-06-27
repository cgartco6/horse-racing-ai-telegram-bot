import os
from dotenv import load_dotenv
import pytz

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("7881119044:AAG8QVhVD-muuIGAnTu4EjZHdDfdVRrwAQY")
CHANNEL_ID = os.getenv("-1002722776313")
TIMEZONE = pytz.timezone(os.getenv("TIMEZONE", "Europe/London"))

# AI Model Parameters
MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0")
MIN_TRAINING_SAMPLES = int(os.getenv("MIN_TRAINING_SAMPLES", 1000))
FEATURES = [
    'horse_age', 'jockey_win_rate', 'trainer_win_rate', 
    'weight', 'distance_suitability', 'track_record',
    'going_preference', 'days_since_last_run', 'recent_form',
    'injury_risk', 'news_sentiment'
]

TRACKS = ["Ascot", "Goodwood", "York", "Newmarket", "Doncaster"]
