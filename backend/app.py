from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)


model = pickle.load(open("heart_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

FEATURES = [
    "BMI",
    "Smoking",
    "AlcoholDrinking",
    "Stroke",
    "PhysicalHealth",
    "MentalHealth",
    "DiffWalking",
    "Sex",
    "AgeCategory",
    "Race",
    "Diabetic",
    "PhysicalActivity",
    "GenHealth",
    "SleepTime",
    "Asthma",
    "KidneyDisease",
    "SkinCancer"
]

@app.route("/")
def home():
    return "LifeScanAI Backend Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    try:
        input_data = [data[f] for f in FEATURES]
        input_array = np.array(input_data).reshape(1, -1)
        scaled = scaler.transform(input_array)

        prediction = model.predict(scaled)[0]

        result = "High Risk of Heart Disease" if prediction == 1 else "Low Risk of Heart Disease"

        return jsonify({
            "prediction": int(prediction),
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
