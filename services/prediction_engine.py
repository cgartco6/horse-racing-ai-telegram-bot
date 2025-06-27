import numpy as np
import pandas as pd
from datetime import datetime
from config.settings import TRACKS, TIMEZONE
from models.prediction_model import RacingModel
from utils.formatters import generate_race_id

class PredictionEngine:
    def __init__(self):
        self.model = RacingModel()
        self.model.model = joblib.load('models/prod_model.pkl')
        
    def generate_daily_races(self):
        races = {}
        for track in TRACKS:
            races[track] = [self._create_race(track) for _ in range(6)]
        return races
    
    def _create_race(self, track):
        return {
            'race_id': generate_race_id(track),
            'track': track,
            'time': datetime.now(TIMEZONE).strftime("%H:%M"),
            'distance': self._get_distance(track),
            # ... other race parameters
        }
    
    def predict_race(self, race_data):
        predictions = self.model.predict(race_data['participants'])
        # Add bookmaker simulations
        race_data['predictions'] = self._apply_bookmaker_adjustments(predictions)
        return race_data
    
    def _apply_bookmaker_adjustments(self, predictions):
        # Hollywoodbets and Betway simulation algorithms
        df = pd.DataFrame(predictions)
        df['hollywoodbets'] = df['ai_win_prob'] * np.random.uniform(0.85, 1.15, len(df))
        df['betway'] = df['ai_win_prob'] * np.random.uniform(0.8, 1.2, len(df))
        return df
