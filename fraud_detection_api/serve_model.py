import sys
sys.path.append('../')
from flask import Flask, request, jsonify
import joblib
import numpy as np
from preprocess_input import preprocess_input
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load("../models/rfc_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    
    # Preprocess the input
    preprocessed_data = preprocess_input(data)
    
    # Make a prediction
    prediction = model.predict(preprocessed_data)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
