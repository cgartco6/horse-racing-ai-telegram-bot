import pandas as pd
from config.settings import FEATURES

def load_historical_data(file_path='data/historical_results.csv'):
    try:
        df = pd.read_csv(file_path)
        # Ensure we have the required columns
        required_columns = FEATURES + ['outcome']
        if set(required_columns).issubset(df.columns):
            return df
        else:
            raise ValueError("Historical data is missing required columns.")
    except FileNotFoundError:
        # Return empty DataFrame with required columns
        return pd.DataFrame(columns=required_columns)

def save_historical_data(df, file_path='data/historical_results.csv'):
    df.to_csv(file_path, index=False)
