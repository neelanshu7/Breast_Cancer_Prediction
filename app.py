from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load your trained model and scaler
model = joblib.load('randomforestModel.pkl')  # Use your actual model file
scaler = joblib.load('scaler.pkl')              # Scaler if used

@app.route('/')
def home():
    return render_template('prediction.html')

@app.route('/prediction.html', methods=['POST'])
def predict():
    # Collect data from form
    try:
        age = float(request.form['Age'])
        menopause = int(request.form['Menopause'])
        tumor_size = float(request.form['TumorSize'])
        inv = int(request.form['INV'])
        metastasis = int(request.form['Metastasis'])
        breast = int(request.form['Breast'])
        breast_quadrant = int(request.form['BreastQuadrant'])
        history = int(request.form['History'])

        features = np.array([[age, menopause, tumor_size, inv, metastasis, breast, breast_quadrant, history]])
        scaled_features = scaler.transform(features)

        prediction = model.predict(scaled_features)[0]
        result = "Malignant" if prediction == 1 else "Benign"

        return render_template('report.html', 
                               result=result,
                               age=age, menopause=menopause, tumor_size=tumor_size, 
                               inv=inv, metastasis=metastasis, breast=breast, 
                               breast_quadrant=breast_quadrant, history=history)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
