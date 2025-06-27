import pandas as pd
import numpy as np
from .prediction_model import RacingModel
from config.settings import MIN_TRAINING_SAMPLES
from services.data_loader import load_historical_data, save_historical_data

class LearningSystem:
    def __init__(self):
        self.model = RacingModel()
        self.historical_data = load_historical_data()
        
    def update_model(self, new_results):
        # Append new results to historical data
        updated_data = pd.concat([self.historical_data, new_results])
        save_historical_data(updated_data)
        
        # Retrain if enough new samples
        if len(updated_data) > MIN_TRAINING_SAMPLES:
            self.model.train(updated_data)
            
    def analyze_failures(self):
        # Analyze prediction errors to improve feature engineering
        if 'predicted_outcome' in self.historical_data.columns:
            predictions = self.historical_data[self.historical_data['predicted_outcome'].notna()]
            errors = predictions[predictions['outcome'] != predictions['predicted_outcome']]
            # Here we can add logic to analyze errors and adjust feature weights or add new features
            return errors
        else:
            return pd.DataFrame()
