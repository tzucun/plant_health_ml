
```markdown
# Plant Health Prediction (ML)

This repository contains a Machine Learning project designed to predict the health status of a plant based on various environmental and soil parameters.

This project was developed by **Group 3** from the **Machine Learning** course, Informatics Engineering, Faculty of Computer Science, **Sriwijaya University**.

## 👥 Team Members (Group 3)

* **Mevika Vania** (09021182328010)
* **Stanley Gilbert Lionardi** (09021282328042)
* **Charlistio Aditirta Wijaya** (09021282328064)
* **Andreas Calvin** (09021282328066)
* **Fitran Husein** (09021382328148)

## 🛠️ Tech Stack

* **Language**: Python 3.10.10
* **Environment**: Google Colab (Model Training)
* **Libraries**: Scikit-learn, Pandas, NumPy, etc.

## 📂 Repository Structure

* `dataset/`: Contains the dataset used for training and testing.
* `models/`: Saved trained models (e.g., `.pkl` or `.h5` files).
* `src/`: Source code for data preprocessing and model training.
* `app.py`: Main application script (e.g., for Web Interface/API).
* `predict.py`: Script to run predictions on new data.

## 📊 Features / Input Parameters

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

## 🚀 Usage

To use the model for prediction, ensure you have the necessary dependencies installed.

### Sample Prediction Code

You can use the `predict.py` script or import the model in your Python script. Below is an example of the data format required for a "Healthy" classification:

```python
# Sample input data
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

# Pass this sample to your model's predict function
# Expected Output: healthy

```

### Running the Application

If you are using the provided scripts:

```bash
# Example command to run the app
python app.py

```

## 📝 License

This project is for educational purposes under the Faculty of Computer Science, Sriwijaya University.

```

```
