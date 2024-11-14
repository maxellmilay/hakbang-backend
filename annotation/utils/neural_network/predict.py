# load_and_predict.py
import torch
import pandas as pd
import joblib

import os
from dotenv import load_dotenv

from annotation.utils.neural_network.larger_nn import LargerNN

load_dotenv()

def predict(input_data):
    df = pd.DataFrame(input_data)

    # Initialize the model and load the state dictionary
    model = LargerNN()
    model.load_state_dict(torch.load(f'models/{os.getenv('LATEST_NN_MODEL_NAME')}', weights_only=True))
    model.eval()  # Set to evaluation mode

    # Prepare the features for prediction
    X_sample = df[['weather_condition', 'urban_density', 'sidewalk_capacity', 'safety_risk']].values

    # Import scaler
    scaler = joblib.load(f'models/{os.getenv('LATEST_NN_SCALER_NAME')}')
    X_sample = scaler.transform(X_sample)

    # Convert to PyTorch tensor
    X_sample_tensor = torch.tensor(X_sample, dtype=torch.float32)

    # Predict using the model and apply sigmoid to get a probability
    with torch.no_grad():
        output = model(X_sample_tensor)
        predicted_accessibility_probability = torch.sigmoid(output).item()  # Convert to probability for binary classification

    return predicted_accessibility_probability
