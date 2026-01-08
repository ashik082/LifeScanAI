Note: The .pkl files are shared for academic project purposes and should only be loaded if the source is trusted.

# LifeScanAI – Machine Learning Fueled Diagnostics

LifeScanAI is a machine learning–based web application designed to predict the risk of heart disease using user-provided health, lifestyle, and demographic data. The project integrates a trained ML model with a Flask backend and a clean, interactive frontend to provide instant risk assessment.


## Problem Statement

Traditional heart disease risk assessment requires clinical tests and expert evaluation, which may not always be easily accessible. There is a need for a lightweight system that can provide preliminary risk analysis using available health indicators.

---

## Proposed Solution

LifeScanAI uses a supervised machine learning model trained on a large public health dataset to predict whether a person is at high or low risk of heart disease. Users input their health parameters through a web interface, and the system returns an instant prediction.

---

## Technologies Used

### Machine Learning
- Python
- Pandas, NumPy
- Scikit-learn
- Logistic Regression
- StandardScaler

### Backend
- Flask
- Flask-CORS
- Pickle (model serialization)

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)
- LocalStorage (for prediction history)


## Deployment

- **Backend:** Deployed on [Render](https://lifescanai.onrender.com/)
- **Frontend:** Deployed on [Netlify](https://lifescanai.netlify.app/)


## Project Structure

LifeScanAI/
│
├── backend/
│ ├── app.py
│ ├── heart_model.pkl
│ ├── scaler.pkl
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── history.html
│ ├── predict.html
│ └── common-styles.css
│
├── training/
│ ├── train_model.ipynb
│ └── heart_large.csv
│
└── README.md

## Model Details

Algorithm: Logistic Regression
Train-Test Split: 80% Training / 20% Testing
Task: Binary Classification (Heart Disease Risk)
Output:
  High Risk of Heart Disease
  Low Risk of Heart Disease

## Data Privacy Note

This application does not store user data on a server or database. Prediction history is stored locally in the browser using LocalStorage and can be cleared at any time.

## ⚠️ Disclaimer

This project is intended for educational and research purposes only. It is not a medical diagnosis tool and should not be used as a substitute for professional medical advice.

## References
-> CDC Heart Disease Dataset
-> Scikit-learn Documentation
-> Flask Documentation
