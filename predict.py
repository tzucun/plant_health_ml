import joblib
import numpy as np

# Load model & scaler SVM
model = joblib.load("../models/model_svm.pkl")
scaler = joblib.load("../models/scaler.pkl")

def predict_plant(data):
    """
    data harus berurutan sesuai training:
    [
        Soil_Moisture,
        Ambient_Temperature,
        Soil_Temperature,
        Humidity,
        Light_Intensity,
        Soil_pH,
        Nitrogen_Level,
        Phosphorus_Level,
        Potassium_Level,
        Chlorophyll_Content,
        Electrochemical_Signal
    ]
    """

    data = np.array(data).reshape(1, -1)
    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)[0]
    probability = model.predict_proba(data_scaled)[0]

    return prediction, probability


# Contoh prediksi manual
if __name__ == "__main__":
    sample = [
        45.2,   # Soil_Moisture
        29.5,   # Ambient_Temperature
        27.8,   # Soil_Temperature
        70.0,   # Humidity
        1200,   # Light_Intensity
        6.5,    # Soil_pH
        40,     # Nitrogen_Level
        25,     # Phosphorus_Level
        30,     # Potassium_Level
        55.4,   # Chlorophyll_Content
        0.87    # Electrochemical_Signal
    ]

    pred, proba = predict_plant(sample)

    print("Prediksi Kelas :", pred)
    print("Probabilitas  :", proba)
