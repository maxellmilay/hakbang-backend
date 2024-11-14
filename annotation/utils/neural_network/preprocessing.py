import torch
import pandas as pd
import joblib

import os
from dotenv import load_dotenv

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

load_dotenv()

def generate_nn_training_data(data):
    print('Preprocessing FIS Data into train and test sets...')

    df = pd.DataFrame(data)

    # Split the data into features and target
    X = df[['weather_condition', 'urban_density', 'sidewalk_capacity', 'safety_risk']].values
    y = df['accessibility'].values  # 0 or 1

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print('Exporting scaler...')
    joblib.dump(scaler, f'models/{os.getenv('REMOTE_DB_HOST')}')

    # Convert to PyTorch tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)  # Shape (n_samples, 1)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

    print('Preprocessing Complete!')

    return X_train_tensor, X_test_tensor, y_train_tensor, y_test_tensor
