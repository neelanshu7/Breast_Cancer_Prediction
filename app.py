from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib

app = Flask(__name__)

# Load your trained model and scaler
model = joblib.load('randomforestModel.pkl')  # Use your actual model file
scaler = joblib.load('scaler.pkl')              # Scaler if used

# In-memory storage for patient data (for demonstration purposes)
patient_data_storage = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    # This is a placeholder. In a real application, you'd have login logic here.
    return render_template('index.html')
@app.route('/login.html')
def login():
    # This is a placeholder. In a real application, you'd have login logic here.
    return render_template('login.html')

@app.route('/about.html')
def about():
    # This is a placeholder. You'd have content for the about page here.
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    # This is a placeholder. You'd have content for the contact page here.
    return render_template('contact.html')

@app.route('/patient-data.html', methods=['GET', 'POST'])
def patient_data():
    if request.method == 'POST':
        # Store patient data
        patient_data_storage['personal'] = {
            'name': request.form['name'],
            'dob': request.form['dob'],
            'age': request.form['age'],
            'sex': request.form['sex']
        }
        patient_data_storage['guardian'] = {
            'father_name': request.form['father-name'],
            'mother_name': request.form['mother-name'],
            'guardian_name': request.form.get('gurdian-name', '')
        }
        patient_data_storage['contact'] = {
            'phone': request.form['phone'],
            'emergency_contact': request.form.get('emergency-contact', ''),
            'country': request.form['country'],
            'state': request.form['state'],
            'address': request.form['address']
        }
        return redirect(url_for('prediction'))
    return render_template('patient-data.html')

@app.route('/prediction.html', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Store prediction input data as strings from form
        raw_data = {
            'age': int(request.form['Age']),
            'menopause': int(request.form['Menopause']),
            'tumor_size': float(request.form['TumorSize']),
            'inv': int(request.form['INV']),
            'metastasis': int(request.form['Metastasis']),
            'breast': int(request.form['Breast']),
            'breast_quadrant': int(request.form['BreastQuadrant']),
            'history': int(request.form['History'])
        }

        patient_data_storage['prediction_input'] = raw_data

        # Ensure order matches model training
        features = np.array([[raw_data['age'], raw_data['menopause'], raw_data['tumor_size'],
                              raw_data['inv'], raw_data['metastasis'], raw_data['breast'],
                              raw_data['breast_quadrant'], raw_data['history']]])

        # Scale and predict
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]
        result = "Malignant" if prediction == 1 else "Benign"

        patient_data_storage['ml_prediction_result'] = result

        return redirect(url_for('report'))
    return render_template('prediction.html')

@app.route('/report.html')
def report():
    # Retrieve all stored data
    personal_data = patient_data_storage.get('personal', {})
    guardian_data = patient_data_storage.get('guardian', {})
    contact_data = patient_data_storage.get('contact', {})
    prediction_input_data = patient_data_storage.get('prediction_input', {})
    ml_prediction_result = patient_data_storage.get('ml_prediction_result', 'N/A')

    return render_template('report.html',
                           personal_data=personal_data,
                           guardian_data=guardian_data,
                           contact_data=contact_data,
                           prediction_input_data=prediction_input_data,
                           ml_prediction_result=ml_prediction_result)
    
if __name__ == '__main__':
    app.run(debug=True)

