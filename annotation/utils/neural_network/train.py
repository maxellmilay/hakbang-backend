import torch
import torch.nn as nn
import torch.optim as optim

from annotation.utils.neural_network.preprocessing import generate_nn_training_data
from annotation.utils.neural_network.larger_nn import LargerNN

def train(n_samples=20000, learning_rate=0.01, num_epochs=300):
    N_SAMPLES = n_samples
    LEARNING_RATE = learning_rate
    NUM_EPOCHS = num_epochs

    X_train_tensor, X_test_tensor, y_train_tensor, y_test_tensor = generate_nn_training_data(N_SAMPLES)

    model = LargerNN()
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(),lr=LEARNING_RATE)

    for epoch in range(NUM_EPOCHS):
        # Forward pass
        outputs = model(X_train_tensor)
        loss = criterion(outputs, y_train_tensor)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{NUM_EPOCHS}], Loss: {loss.item():.4f}')

    # Evaluate on the test data
    with torch.no_grad():
        test_outputs = torch.sigmoid(model(X_test_tensor))  # Apply sigmoid to get probabilities
        predicted = (test_outputs >= 0.5).float()  # Convert probabilities to 0 or 1
        accuracy = (predicted == y_test_tensor).float().mean().item()
        print(f'Test Accuracy: {accuracy * 100:.2f}%')

    # Save the model's state_dict to a .pth file
    torch.save(model.state_dict(), 'models/nn_model.pth')
    print("Model state_dict saved to 'models/nn_model.pth'")
