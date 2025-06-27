import numpy as np
import pandas as pd
from datetime import datetime
import random
from config.settings import TRACKS, TIMEZONE
from models.prediction_model import RacingModel
from utils.formatters import generate_race_id, format_race_time

class PredictionEngine:
    def __init__(self):
        self.model = RacingModel()
        # Simulated data for horses, jockeys, trainers
        self.horses = [f"Horse_{i}" for i in range(1, 101)]
        self.jockeys = [f"Jockey_{i}" for i in range(1, 31)]
        self.trainers = [f"Trainer_{i}" for i in range(1, 21)]
        
    def generate_daily_races(self):
        races = {}
        for track in TRACKS:
            races[track] = [self._create_race(track) for _ in range(6)]
        return races
    
    def _create_race(self, track):
        # Generate a race time between 13:00 and 17:00
        hour = random.randint(13, 16)
        minute = random.choice([0, 15, 30, 45])
        time_str = f"{hour}:{minute:02d}"
        
        return {
            'race_id': generate_race_id(track),
            'track': track,
            'time': format_race_time(time_str),
            'distance': self._get_distance(track),
            'going': random.choice(["Good", "Soft", "Heavy", "Firm"]),
            'weather': random.choice(["Sunny", "Cloudy", "Rainy"]),
            'participants': self._generate_participants(8, track)  # 8 participants
        }
    
    def _get_distance(self, track):
        # Assign typical distances for each track
        distances = {
            "Ascot": [1000, 1200, 1600, 2000, 2400],
            "Goodwood": [1200, 1400, 1600, 2000],
            "York": [1400, 1600, 2000, 2400],
            "Newmarket": [1200, 1400, 1600, 2000],
            "Doncaster": [1600, 2000, 2400, 2800]
        }
        return random.choice(distances[track])
    
    def _generate_participants(self, num, track):
        participants = []
        for _ in range(num):
            horse = random.choice(self.horses)
            jockey = random.choice(self.jockeys)
            trainer = random.choice(self.trainers)
            participant = {
                'horse': horse,
                'jockey': jockey,
                'trainer': trainer,
                'horse_age': random.randint(3, 8),
                'jockey_win_rate': round(random.uniform(0.05, 0.35), 3),
                'trainer_win_rate': round(random.uniform(0.1, 0.4), 3),
                'weight': random.randint(50, 65),
                'distance_suitability': round(random.uniform(0.5, 1.0), 2),
                'track_record': round(random.uniform(0.3, 0.9), 2),
                'going_preference': round(random.uniform(0.4, 1.0), 2),
                'days_since_last_run': random.randint(14, 120),
                'recent_form': round(random.uniform(0.2, 0.95), 2),
                'injury_risk': round(random.uniform(0.01, 0.2), 2),
                'news_sentiment': round(random.uniform(-0.5, 0.8), 2)
            }
            participants.append(participant)
        return participants
    
    def predict_race(self, race_data):
        df_participants = pd.DataFrame(race_data['participants'])
        # Get AI win probabilities
        ai_probs = self.model.predict(df_participants)
        df_participants['ai_win_prob'] = ai_probs
        # Normalize
        df_participants['ai_win_prob'] = df_participants['ai_win_prob'] / df_participants['ai_win_prob'].sum()
        
        # Simulate bookmaker odds
        df_participants['hollywoodbets'] = df_participants['ai_win_prob'] * np.random.uniform(0.85, 1.15, len(df_participants))
        df_participants['betway'] = df_participants['ai_win_prob'] * np.random.uniform(0.8, 1.2, len(df_participants))
        # Normalize bookmaker probabilities
        df_participants['hollywoodbets'] = df_participants['hollywoodbets'] / df_participants['hollywoodbets'].sum()
        df_participants['betway'] = df_participants['betway'] / df_participants['betway'].sum()
        
        # Sort by AI probability
        df_participants = df_participants.sort_values('ai_win_prob', ascending=False)
        race_data['predictions'] = df_participants.to_dict('records')
        return race_data
