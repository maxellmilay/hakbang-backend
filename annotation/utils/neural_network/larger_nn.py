import torch
import torch.nn as nn

class LargerNN(nn.Module):
    def __init__(self):
        super(LargerNN, self).__init__()
        self.fc1 = nn.Linear(4, 256)    # Increased input layer to 256 neurons
        self.fc2 = nn.Linear(256, 128)  # Second layer with 128 neurons
        self.fc3 = nn.Linear(128, 64)   # Third layer with 64 neurons
        self.fc4 = nn.Linear(64, 32)    # Fourth layer with 32 neurons
        self.fc5 = nn.Linear(32, 16)    # Fifth layer with 16 neurons
        self.fc6 = nn.Linear(16, 8)     # Sixth layer with 8 neurons
        self.fc7 = nn.Linear(8, 4)      # Seventh layer with 4 neurons
        self.fc8 = nn.Linear(4, 1)      # Output layer for binary classification
        self.dropout = nn.Dropout(0.3)  # Increased dropout rate to 30%

    def forward(self, x):
        x = torch.relu(self.fc1(x))    # Activation for first layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc2(x))    # Activation for second layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc3(x))    # Activation for third layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc4(x))    # Activation for fourth layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc5(x))    # Activation for fifth layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc6(x))    # Activation for sixth layer
        x = self.dropout(x)            # Apply dropout
        x = torch.relu(self.fc7(x))    # Activation for seventh layer
        x = self.fc8(x)                # Output layer without activation
        return x