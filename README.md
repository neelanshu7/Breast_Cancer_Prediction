# 🧠 Breast Cancer Detection using Machine Learning

### 🔗 Live Website: [PinkNeuron](https://breast-cancer-prediction-uskp.onrender.com)

This project uses supervised machine learning to detect breast cancer recurrence based on medical features such as tumor size, age, menopause status, and more. It aims to assist in early diagnosis and decision-making for better patient outcomes.

---

## 📁 About This Repository

This repository contains:
- 📓 Jupyter Notebooks for model training and evaluation (located in the `notebook/` directory)
- 📊 Sample datasets (`.csv` files) for training and testing
- 🌐 Flask-based web application for user interaction

---

## 📊 Dataset

- Breast cancer dataset with the following key features:
  - `Age`
  - `Menopause`
  - `Tumor Size`
  - `Inv-Nodes`
  - `Breast` (left/right)
  - `Breast Quadrant` (location)
  - `History` (recurrence history)

- Target:
  - `Diagnosis`: `Benign` or `Malignant`

---
## 📌 Project Structure
```php
project/
│
├── app.py
├── randomforestModel.pkl
├── label_encoder.pkl
├── scaler.pkl
├── requirments.txt
├── 📂 templates/
│   ├── index.html
│   ├── login.html
│   ├── patient-data.html
│   ├── prediction.html
│   ├── report.html
│   ├── about.html
│   └── contact.html 
├── 📂 static/
│   ├── style.css
│   ├── home.png
│   ├── logo.png
│   └── Breast_Cancer_Prediction_using_AI_and_ML.mp4

```
---
## 📂 ML Model

- `Breast-Cancer-Prediction.ipynb` — Data preprocessing, model training, evaluation and prediction
- `breast-cancer-dataset.csv` — Dataset
- `randomforestModel.pkl` — Trained Random Forest model
- `scaler.pkl` — Feature scaler
- `label_encoder.pkl` — Encoders for categorical variables
---
## 💻 How to Run the Project Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/plantalytics.git
   git clone https://github.com/neelanshu7/crop-classification-and-yield-prediction.git
   cd crop-classification-and-yield-prediction

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Flask server:**
   ```bash
   flask run --host=0.0.0.0

4. Access the application:
   Open your browser and navigate to **http://localhost:5000/**
