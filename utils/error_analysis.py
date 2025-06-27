import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

def analyze_prediction_errors(historical_data):
    """Analyze model errors to identify improvement areas"""
    report = {}
    
    # Confusion matrix analysis
    y_true = historical_data['outcome']
    y_pred = historical_data['predicted_outcome']
    cm = confusion_matrix(y_true, y_pred)
    report['confusion_matrix'] = cm.tolist()
    
    # Classification report
    clf_report = classification_report(y_true, y_pred, output_dict=True)
    report['classification_report'] = clf_report
    
    # Feature error correlation
    error_corr = historical_data.corr()['prediction_error'].sort_values(ascending=False)
    report['error_correlations'] = error_corr.to_dict()
    
    # Track-specific errors
    track_errors = historical_data.groupby('track')['prediction_error'].mean().sort_values(ascending=False)
    report['track_errors'] = track_errors.to_dict()
    
    # Jockey performance analysis
    jockey_errors = historical_data.groupby('jockey')['prediction_error'].mean().sort_values()
    report['jockey_errors'] = jockey_errors.head(10).to_dict()
    
    return report

def generate_improvement_plan(error_report):
    """Create actionable improvement plan based on error analysis"""
    plan = []
    
    # Accuracy issues
    accuracy = error_report['classification_report']['accuracy']
    if accuracy < 0.75:
        plan.append(f"Improve model accuracy (current: {accuracy:.2%}) by feature engineering")
    
    # Track-specific issues
    for track, error in error_report['track_errors'].items():
        if error > 0.3:
            plan.append(f"Investigate track-specific patterns for {track} (error: {error:.2f})")
    
    # Feature importance
    for feature, corr in error_report['error_correlations'].items():
        if abs(corr) > 0.2:
            plan.append(f"Review feature '{feature}' handling (error correlation: {corr:.2f})")
    
    return plan
