import streamlit as st
import numpy as np
import joblib

# LOAD MODEL & SCALER
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(page_title="Plant Stress Classification", layout="centered")
st.title("🌱 Plant Health Classification")

st.write("Masukkan parameter kondisi tanaman untuk memprediksi tingkat stres.")

# INPUT 11 FITUR
Soil_Moisture = st.number_input("Soil Moisture (%)", 0.0, 100.0)
Ambient_Temperature = st.number_input("Ambient Temperature (°C)", 0.0, 60.0)
Soil_Temperature = st.number_input("Soil Temperature (°C)", 0.0, 60.0)
Humidity = st.number_input("Humidity (%)", 0.0, 100.0)
Light_Intensity = st.number_input("Light Intensity (lux)", 0.0, 100000.0)
Soil_pH = st.number_input("Soil pH", 0.0, 14.0)
Nitrogen_Level = st.number_input("Nitrogen Level (mg/kg)", 0.0, 1000.0)
Phosphorus_Level = st.number_input("Phosphorus Level (mg/kg)", 0.0, 1000.0)
Potassium_Level = st.number_input("Potassium Level (mg/kg)", 0.0, 1000.0)
Chlorophyll_Content = st.number_input("Chlorophyll Content (%)", 0.0, 100.0)
Electrochemical_Signal = st.number_input("Electrochemical Signal (V)", 0.0, 5.0)

# LABEL KELAS
class_labels = ["Healthy", "Moderate Stress", "High Stress"]

# PREDIKSI
if st.button("Prediksi"):
    data = np.array([
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
    ]).reshape(1, -1)

    # Scaling
    data_scaled = scaler.transform(data)

    # Prediksi probabilitas
    probabilities = model.predict_proba(data_scaled)[0]
    pred_index = np.argmax(probabilities)

    predicted_class = class_labels[pred_index]
    predicted_proba = probabilities[pred_index]

    # OUTPUT
    st.subheader(f"🌿 Status Tanaman: **{predicted_class}**")
    st.write(f"Tingkat Keyakinan Model: **{predicted_proba*100:.2f}%**")
