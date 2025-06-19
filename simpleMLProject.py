import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

print("Libraries imported successfully!")

# Generate a simple synthetic dataset
X, y = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=42)
print(f"Dataset shape: X={X.shape}, y={y.shape}")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train a simple logistic regression model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Make a prediction for the first test sample
sample_prediction = model.predict(X_test[:1])
print(f"Prediction for first test sample: {sample_prediction[0]}")
print("Model trained and prediction made successfully!")