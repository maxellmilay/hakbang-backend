import torch
import torch.nn as nn

class LargerNN(nn.Module):
    def __init__(self):
        super(LargerNN, self).__init__()
        self.fc1 = nn.Linear(4, 64)    # Increase input layer to 64 neurons
        self.fc2 = nn.Linear(64, 32)   # Second layer with 32 neurons
        self.fc3 = nn.Linear(32, 16)   # Third layer with 16 neurons
        self.fc4 = nn.Linear(16, 1)    # Output layer for binary classification
        self.dropout = nn.Dropout(0.2) # Dropout layer with 20% dropout rate

    def forward(self, x):
        x = torch.relu(self.fc1(x))    # Activation for first layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc2(x))    # Activation for second layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc3(x))    # Activation for third layer
        x = self.fc4(x)                # Output layer without activation
        return x
