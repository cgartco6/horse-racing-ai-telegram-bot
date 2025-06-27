import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from config.settings import FEATURES, MODEL_VERSION
from utils.logger import setup_logger

logger = setup_logger()

def retrain_model():
    """Retrain model with latest data"""
    try:
        # Load training data
        data = pd.read_csv('data/model_training_data.csv')
        if len(data) < 500:
            logger.warning("Insufficient data for retraining")
            return False
        
        # Prepare data
        X = data[FEATURES]
        y = data['outcome']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        # Train new model
        model = GradientBoostingClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            random_state=42
        )
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        logger.info(f"Model retrained | Accuracy: {accuracy:.2%}")
        
        # Save new model
        model_path = f'models/model_v{MODEL_VERSION}.pkl'
        joblib.dump(model, model_path)
        
        return accuracy
    except Exception as e:
        logger.error(f"Retraining failed: {str(e)}")
        return False
