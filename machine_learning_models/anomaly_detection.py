import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# Generate synthetic data for demonstration
# Assuming normal data follows a Gaussian distribution
np.random.seed(42)
normal_data = np.random.normal(loc=0.0, scale=1.0, size=(1000, 10))
anomalous_data = np.random.normal(loc=5.0, scale=1.0, size=(50, 10))

# Scale the data to [0, 1]
scaler = MinMaxScaler()
normal_data = scaler.fit_transform(normal_data)
anomalous_data = scaler.transform(anomalous_data)

# Define an autoencoder model
input_dim = normal_data.shape[1]
encoding_dim = 5

input_layer = Input(shape=(input_dim,))
encoder = Dense(encoding_dim, activation="relu")(input_layer)
decoder = Dense(input_dim, activation="sigmoid")(encoder)
autoencoder = Model(inputs=input_layer, outputs=decoder)

# Compile the model
autoencoder.compile(optimizer="adam", loss="mse")

# Train the model on normal data
autoencoder.fit(normal_data, normal_data, epochs=50, batch_size=32, shuffle=True, validation_split=0.1)

# Make predictions and compute reconstruction error on test data
reconstructed_normal = autoencoder.predict(normal_data)
reconstructed_anomalous = autoencoder.predict(anomalous_data)

# Calculate reconstruction error
mse_normal = mean_squared_error(normal_data, reconstructed_normal)
mse_anomalous = mean_squared_error(anomalous_data, reconstructed_anomalous)

# Set threshold as the max MSE of normal data reconstruction
threshold = np.max(mse_normal)
print("Anomaly Detection Threshold:", threshold)

# Detect anomalies
is_anomalous = mse_anomalous > threshold
print("Anomalies detected:", np.sum(is_anomalous))
