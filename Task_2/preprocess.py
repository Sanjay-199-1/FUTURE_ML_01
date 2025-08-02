from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def preprocess_data(df):
    # Drop irrelevant columns
    df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
    
    # One-hot encoding
    df = pd.get_dummies(df, columns=['Geography', 'Gender'], drop_first=True)
    
    # Separate features and target
    X = df.drop('Exited', axis=1)
    y = df['Exited']
    
    return X, y
