from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import bz2  # ✅ For loading .bz2 compressed model
import joblib

app = Flask(__name__)

# ✅ Load the compressed .pkl.bz2 model
try:
    with bz2.BZ2File('forecasting_co2_emmision.pkl.bz2', 'rb') as f:
        model = joblib.load(f)
except Exception as e:
    model = None
    print("❌ Error loading model:", e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return "Model not loaded. Please check the .bz2 file."

        # Extract input values from the form
        features = [float(x) for x in request.form.values()]
        input_array = np.array([features])
        prediction = model.predict(input_array)[0]

        return render_template('index.html', prediction_text=f'Predicted CO₂ Emission: {round(prediction, 2)} tons per capita')
    except Exception as e:
        return f"❌ Error during prediction: {e}"

if __name__ == '__main__':
    app.run(debug=True)
