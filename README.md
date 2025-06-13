# 🧠 Breast Cancer Detection using Machine Learning

This project uses supervised machine learning to detect breast cancer recurrence based on medical features such as tumor size, age, menopause status, and more. It aims to assist in early diagnosis and decision-making for better patient outcomes.

---

## 📂 Project Structure

- `Breast-Cancer.ipynb` — Data preprocessing, model training, and evaluation
- `randomforestModel.pkl` — Trained Random Forest model
- `scaler.pkl` — Feature scaler
- `le_breast.pkl`, `le_bq.pkl`, `le_diag.pkl` — Encoders for categorical variables
- `predict.py` — Interactive terminal prediction script

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

## 🚀 How to Run

### ✅ 1. Clone the repository
```bash
git clone https://github.com/your-username/breast-cancer-detection.git
cd breast-cancer-detection
