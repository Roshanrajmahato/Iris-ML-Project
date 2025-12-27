# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np


app = Flask(__name__)
CORS(app) # allow requests from React dev server


# Load model
model = joblib.load('model/iris_model.pkl')


FEATURE_NAMES = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']


@app.route('/')
def index():
    return jsonify({'message': 'Iris prediction API is running'})


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Expect JSON like: {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    try:
        features = [float(data[name]) for name in FEATURE_NAMES]
    except Exception as e:
        return jsonify({'error': 'Invalid input. Provide sepal_length, sepal_width, petal_length, petal_width'}), 400


    arr = np.array(features).reshape(1, -1)
    pred_class = int(model.predict(arr)[0])
    pred_proba = model.predict_proba(arr).tolist()[0]


    # Map class index to name
    class_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}


    return jsonify({
    'prediction_index': pred_class,
    'prediction': class_map.get(pred_class, str(pred_class)),
    'probabilities': pred_proba
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)