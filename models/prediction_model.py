import joblib
import pandas as pd
import os
from sklearn.ensemble import GradientBoostingClassifier
from config.settings import FEATURES, MIN_TRAINING_SAMPLES
from services.data_loader import load_historical_data, save_historical_data

class RacingModel:
    def __init__(self):
        self.model = GradientBoostingClassifier(n_estimators=300, 
                                              random_state=42,
                                              max_depth=5)
        self.features = FEATURES
        self.model_path = 'models/prod_model.pkl'
        
    def train(self, training_data=None):
        if training_data is None:
            training_data = load_historical_data()
        if len(training_data) < MIN_TRAINING_SAMPLES:
            return False
        X = training_data[self.features]
        y = training_data['outcome']
        self.model.fit(X, y)
        joblib.dump(self.model, self.model_path)
        return True
        
    def predict(self, race_data):
        if not os.path.exists(self.model_path):
            self.train()
        self.model = joblib.load(self.model_path)
        X = pd.DataFrame(race_data)[self.features]
        return self.model.predict_proba(X)[:, 1]
