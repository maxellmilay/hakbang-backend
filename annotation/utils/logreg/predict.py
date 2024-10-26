# Function to get predicted probabilities
def get_logreg_probabilities(model, val):
    return model.predict_proba(val)
