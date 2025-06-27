import pandas as pd
import joblib
from config.settings import FEATURES, MODEL_VERSION, HISTORICAL_DATA_FILE
from utils.logger import setup_logger

logger = setup_logger()

def load_training_data():
    """Load training data with validation"""
    try:
        data = pd.read_csv(HISTORICAL_DATA_FILE)
        required_cols = FEATURES + ['outcome']
        
        if not set(required_cols).issubset(data.columns):
            logger.error("Missing columns in training data")
            return None
        
        return data[required_cols]
    except Exception as e:
        logger.error(f"Data loading failed: {str(e)}")
        return None

def load_production_model():
    """Load current production model"""
    try:
        model_path = f'models/model_v{MODEL_VERSION}.pkl'
        return joblib.load(model_path)
    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")
        return None
