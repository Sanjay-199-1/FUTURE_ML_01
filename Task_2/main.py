from load_data import load_data
from preprocess import preprocess_data
from train_model import train_xgboost
from evaluate import evaluate_model

# Step 1: Load
df = load_data('Churn_Modelling.csv')

# Step 2: Preprocess
X, y = preprocess_data(df)

# Step 3: Train
model, X_test, y_test = train_xgboost(X, y)

# Step 4: Evaluate
evaluate_model(model, X_test, y_test)
