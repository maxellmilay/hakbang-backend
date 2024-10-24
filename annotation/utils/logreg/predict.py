# Function to get predicted probabilities
def get_probabilities(model, val):
  return model.predict_log_proba(val)
