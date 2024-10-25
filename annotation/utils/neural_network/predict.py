# load_and_predict.py
import torch
import pandas as pd
from sklearn.preprocessing import StandardScaler

from annotation.utils.neural_network.larger_nn import LargerNN

def predict(input_data):
    df = pd.DataFrame(input_data)

    # Initialize the model and load the state dictionary
    model = LargerNN()
    model.load_state_dict(torch.load('models/nn_model.pth'))
    model.eval()  # Set to evaluation mode

    # Prepare the features for prediction
    X_sample = df[['weather_condition', 'urban_density', 'sidewalk_capacity', 'safety_risk']].values

    # Standardize the features using the scaler
    scaler = StandardScaler()
    X_sample = scaler.transform(X_sample)

    # Convert to PyTorch tensor
    X_sample_tensor = torch.tensor(X_sample, dtype=torch.float32)

    # Predict using the model and apply sigmoid to get a probability
    with torch.no_grad():
        output = model(X_sample_tensor)
        predicted_accessibility_probability = torch.sigmoid(output)  # Convert to probability for binary classification


    print(f"Predicted Accessibility: ", predicted_accessibility_probability)

    return predicted_accessibility_probability
