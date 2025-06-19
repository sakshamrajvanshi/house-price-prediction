import os
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Correct absolute path to the model
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebook', 'model', 'price_model.pkl'))

# Load model
model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            rm = float(request.form.get("RM", ""))
            lstat = float(request.form.get("LSTAT", ""))
            ptratio = float(request.form.get("PTRATIO", ""))
            features = np.array([[rm, lstat, ptratio]])
            prediction_value = model.predict(features)[0]
            prediction = f"Predicted House Price: ${prediction_value * 1000:.2f}"

        except ValueError:
            error = "❌ Please enter valid numeric values for all fields."

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
