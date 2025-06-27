import pandas as pd
import numpy as np
from utils.data_generator import generate_historical_data

def refresh_simulated_data():
    """Refresh simulated data files with new records"""
    # Add new results to historical data
    existing = pd.read_csv('data/historical_results.csv')
    new_data = generate_historical_data(100)
    updated = pd.concat([existing, new_data], ignore_index=True)
    updated.to_csv('data/historical_results.csv', index=False)
    
    # Add to training data
    training = pd.read_csv('data/model_training_data.csv')
    training = pd.concat([training, new_data], ignore_index=True)
    training.to_csv('data/model_training_data.csv', index=False)
    
    return len(new_data)
