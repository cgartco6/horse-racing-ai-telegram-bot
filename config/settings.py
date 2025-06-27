import os
import pytz

TELEGRAM_TOKEN = os.getenv("7881119044:AAG8QVhVD-muuIGAnTu4EjZHdDfdVRrwAQY")
CHANNEL_ID = os.getenv("-1002722776313")
TIMEZONE = pytz.timezone("Europe/London")

# AI Model Parameters
MODEL_VERSION = "1.2.0"
MIN_TRAINING_SAMPLES = 1000
FEATURES = [
    'horse_age', 'jockey_win_rate', 'trainer_win_rate', 
    'weight', 'distance_suitability', 'track_record',
    'going_preference', 'days_since_last_run', 'recent_form',
    'injury_risk', 'news_sentiment'
]

TRACKS = ["Ascot", "Goodwood", "York", "Newmarket", "Doncaster"]
