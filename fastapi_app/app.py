from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.losses import MeanSquaredError
from sklearn.preprocessing import StandardScaler

app = FastAPI()

# Dummy scalers and models
scalers = {}
models = {}


# Define input schemas
class AnomalyDetectionInput(BaseModel):
    data: list[float]  # A single data point (features as a list)


class CutSizeInput(BaseModel):
    material_thickness: float
    material_density: float
    desired_precision: float


class FaultIntervalInput(BaseModel):
    temperature: float
    vibration: float
    pressure: float
    rpm: float


# Generate dummy scalers and models for demonstration purposes
def create_anomaly_model():
    input_dim = 10
    encoding_dim = 5
    input_layer = Input(shape=(input_dim,))
    encoder = Dense(encoding_dim, activation="relu")(input_layer)
    decoder = Dense(input_dim, activation="sigmoid")(encoder)
    autoencoder = Model(inputs=input_layer, outputs=decoder)
    autoencoder.compile(optimizer="adam", loss="mse")
    return autoencoder


def create_cut_size_model():
    model = Sequential([
        Dense(64, activation="relu", input_shape=(3,)),
        Dropout(0.2),
        Dense(32, activation="relu"),
        Dropout(0.2),
        Dense(16, activation="relu"),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    return model


def create_fault_interval_model():
    model = Sequential([
        Dense(128, activation="relu", input_shape=(4,)),
        Dropout(0.2),
        Dense(64, activation="relu"),
        Dropout(0.2),
        Dense(32, activation="relu"),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    return model


# Initialize models and scalers
models["anomaly_detection"] = create_anomaly_model()
models["cut_size"] = create_cut_size_model()
models["fault_interval"] = create_fault_interval_model()

scalers["anomaly_detection"] = StandardScaler()
scalers["cut_size"] = StandardScaler()
scalers["fault_interval"] = StandardScaler()

# Dummy fit scalers with random data for example purposes
scalers["anomaly_detection"].fit(np.random.rand(100, 10))
scalers["cut_size"].fit(np.random.rand(100, 3))
scalers["fault_interval"].fit(np.random.rand(100, 4))


@app.post("/predict/anomaly")
async def predict_anomaly(input_data: AnomalyDetectionInput):
    try:
        data = np.array(input_data.data).reshape(1, -1)
        data_scaled = scalers["anomaly_detection"].transform(data)
        reconstruction = models["anomaly_detection"].predict(data_scaled)
        mse = MeanSquaredError()(data_scaled, reconstruction).numpy()
        threshold = 0.1  # Assume a threshold for demonstration
        is_anomaly = mse > threshold
        return {"is_anomaly": bool(is_anomaly), "mse": mse}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict/cut_size")
async def predict_cut_size(input_data: CutSizeInput):
    try:
        data = np.array([input_data.material_thickness, input_data.material_density, input_data.desired_precision]).reshape(1, -1)
        data_scaled = scalers["cut_size"].transform(data)
        cut_size = models["cut_size"].predict(data_scaled).flatten()[0]
        return {"recommended_cut_size": cut_size}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict/fault_interval")
async def predict_fault_interval(input_data: FaultIntervalInput):
    try:
        data = np.array([input_data.temperature, input_data.vibration, input_data.pressure, input_data.rpm]).reshape(1, -1)
        data_scaled = scalers["fault_interval"].transform(data)
        fault_interval = models["fault_interval"].predict(data_scaled).flatten()[0]
        return {"predicted_time_to_fault": fault_interval}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app with: `uvicorn app:app --reload` in the command line
