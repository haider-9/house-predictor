import joblib

model = joblib.load("models/model.pkl")

def predict(features):
    return model.predict([features])[0]