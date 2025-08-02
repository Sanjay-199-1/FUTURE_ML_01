from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import pandas as pd

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1]
    
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("ROC AUC Score:", roc_auc_score(y_test, y_proba))
    
    # Save prediction results
    results = pd.DataFrame({
        'Predicted': y_pred,
        'Churn_Probability': y_proba
    })
    results.to_csv('churn_predictions.csv', index=False)
