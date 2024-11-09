import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

# Generate synthetic data for demonstration purposes
# Simulating features like temperature, vibration, pressure, etc.
np.random.seed(42)
num_samples = 1000

temperature = np.random.uniform(50, 120, num_samples)  # Example in Celsius
vibration = np.random.uniform(0, 0.5, num_samples)  # Vibration in g-forces
pressure = np.random.uniform(5, 30, num_samples)  # Pressure in psi
rpm = np.random.uniform(1000, 5000, num_samples)  # Rotations per minute

# Target interval until machine fault (in hours) with added noise
time_to_fault = (1000 - (temperature * 1.2 + vibration * 100 + pressure * 10 + rpm * 0.05)
                 + np.random.normal(0, 20, num_samples))

# Combine features into a dataset
X = np.stack([temperature, vibration, pressure, rpm], axis=1)
y = time_to_fault

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the regression model
model = Sequential([
    Dense(128, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation="relu"),
    Dropout(0.2),
    Dense(32, activation="relu"),
    Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer="adam", loss="mse")

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.1)

# Make predictions and evaluate the model
y_pred = model.predict(X_test).flatten()
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# Predict time to fault for a new machine status
new_status = np.array([[90, 0.25, 15, 2500]])  # New sensor readings
new_status_scaled = scaler.transform(new_status)
predicted_fault_interval = model.predict(new_status_scaled)
print("Predicted Time to Fault (hours):", predicted_fault_interval[0])
