import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

# Generate synthetic data for demonstration
# Let's assume we have features such as material thickness, density, and desired cut precision
np.random.seed(42)
num_samples = 1000
material_thickness = np.random.uniform(0.1, 10, num_samples)
material_density = np.random.uniform(0.5, 3.5, num_samples)
desired_precision = np.random.uniform(1, 5, num_samples)

# Target cut size (simulated with a simple formula plus some noise)
cut_size = (material_thickness * 2.5 + material_density * 1.8 + desired_precision * 0.5
            + np.random.normal(0, 0.5, num_samples))

# Combine features into a dataset
X = np.stack([material_thickness, material_density, desired_precision], axis=1)
y = cut_size

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build a regression model
model = Sequential([
    Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(32, activation="relu"),
    Dropout(0.2),
    Dense(16, activation="relu"),
    Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer="adam", loss="mse")

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.1)

# Make predictions on the test set
y_pred = model.predict(X_test).flatten()

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

new_material = np.array([[5.5, 2.2, 3.0]])  # New material properties
new_material_scaled = scaler.transform(new_material)
recommended_cut_size = model.predict(new_material_scaled)
print("Recommended Cut Size:", recommended_cut_size[0])
