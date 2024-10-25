
from sklearn.model_selection import train_test_split

# Function to split features and target
def split_features_target(df, test_size):

  """
  df should contain these columns ['Weather Conditions', 'Road Capacity', 'Urban Density', 'Safety Risk', 'Accessibility']
  """

  cols = df.columns
  print(cols)

  classes = cols[-1:]  # Target is 'Accessibility'
  print(classes)
  features = cols[0:4]  # Select the first 4 features
  print(features)

  X = df[features].values
  Y = df[classes].values

  return train_test_split(X, Y, test_size=test_size)
