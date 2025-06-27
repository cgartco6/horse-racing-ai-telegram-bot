import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from config.settings import FEATURES, MIN_TRAINING_SAMPLES

class RacingModel:
    def __init__(self):
        self.model = GradientBoostingClassifier(n_estimators=300, 
                                              random_state=42,
                                              max_depth=5)
        self.features = FEATURES
        
    def train(self, training_data):
        X = training_data[self.features]
        y = training_data['outcome']
        self.model.fit(X, y)
        joblib.dump(self.model, 'models/prod_model.pkl')
        
    def predict(self, race_data):
        X = pd.DataFrame(race_data)[self.features]
        return self.model.predict_proba(X)[:, 1]
