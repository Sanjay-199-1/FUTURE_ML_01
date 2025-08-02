from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_xgboost(X, y, save_path='xgb_model.pkl'):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    
    joblib.dump(model, save_path)
    return model, X_test, y_test
