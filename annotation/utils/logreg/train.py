from sklearn.linear_model import LogisticRegression

# Function to train and evaluate the logistic regression model
def train(X_train, X_test, Y_train, Y_test):
    log_accessibility_model = LogisticRegression(penalty="l2").fit(X_train, Y_train)
    score = log_accessibility_model.score(X_test, Y_test)
    return log_accessibility_model, score

# Add training code
