# Plant Health Prediction (ML)

This repository contains a Machine Learning project designed to predict the health status of a plant based on various environmental and soil parameters. The model is deployed as a web application using **Streamlit**.

This project was developed by **Group 3** from the **Machine Learning** course, Informatics Engineering, Faculty of Computer Science, **Sriwijaya University**.

## 👥 Team Members (Group 3)

* **Mevika Vania** (09021182328010)
* **Stanley Gilbert Lionardi** (09021282328042)
* **Charlistio Aditirta Wijaya** (09021282328064)
* **Andreas Calvin** (09021282328066)
* **Fitran Husein** (09021382328148)

## 🛠️ Tech Stack

* **Language**: Python 3.10.10
* **Framework**: Streamlit
* **Training Environment**: Google Colab
* **Libraries**: Scikit-learn, Pandas, NumPy, etc.

## 📂 Repository Structure

* `dataset/`: Contains the dataset used for training and testing.
* `models/`: Saved trained models (e.g., `.pkl` files).
* `src/`: Source code for data preprocessing and model training.
* `app.py`: Main Streamlit application script.
* `predict.py`: Script to run predictions (backend logic).

## 📊 Input Parameters

The model accepts the following 11 parameters to predict plant health:

1.  **Soil Moisture** (%)
2.  **Ambient Temperature** (°C)
3.  **Soil Temperature** (°C)
4.  **Humidity** (%)
5.  **Light Intensity** (Lux)
6.  **Soil pH**
7.  **Nitrogen Level**
8.  **Phosphorus Level**
9.  **Potassium Level**
10. **Chlorophyll Content**
11. **Electrochemical Signal**

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/tzucun/plant_health_ml.git](https://github.com/tzucun/plant_health_ml.git)
    cd plant_health_ml
    ```

2.  **Install dependencies:**
    (Ensure you have `streamlit` installed)
    ```bash
    pip install streamlit scikit-learn pandas numpy
    ```

3.  **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

## 🧪 Sample Data

Below is an example of the input data format used to classify a plant as **"Healthy"**:

```python
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

# Output: healthy

```

## 📝 License
This project is for educational purposes under the Faculty of Computer Science, Sriwijaya University.
