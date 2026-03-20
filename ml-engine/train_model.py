import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("cpu_dataset.csv")

# Prepare data
X = data[['cpu_usage']]
y = data['cpu_usage']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "cpu_model.pkl")

print("AI model trained and saved as cpu_model.pkl")
