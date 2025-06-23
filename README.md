# 🧠 Breast Cancer Detection using Machine Learning

This project uses supervised machine learning to detect breast cancer recurrence based on medical features such as tumor size, age, menopause status, and more. It aims to assist in early diagnosis and decision-making for better patient outcomes.


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
## 📂 Project Structure
```php
project/
│
├── app.py
├── randomforestModel.pkl
├── label_encoder.pkl
├── scaler.pkl
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── patient-data.html
│   ├── prediction.html
│   ├── report.html
│   ├── about.html
│   └── contact.html 
├── static/
│   ├── style.css
│   ├── home.png
│   ├── logo.png
│   └── Breast_Cancer_Prediction_using_AI_and_ML.mp4

```
## 📂 ML Model

- `Breast-Cancer-Prediction.ipynb` — Data preprocessing, model training, evaluation and prediction
- `breast-cancer-dataset.csv` — Dataset
- `randomforestModel.pkl` — Trained Random Forest model
- `scaler.pkl` — Feature scaler
- `label_encoder.pkl` — Encoders for categorical variables
---
## 🚀 How to Run

