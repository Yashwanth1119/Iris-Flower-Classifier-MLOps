import pickle
import numpy as np

def load_model():
    with open('model/iris_model.pkl', 'rb') as f:
        return pickle.load(f)

def predict(features):
    model = load_model()
    prediction = model.predict([features])
    return prediction[0]
