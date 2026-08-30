from pathlib import Path
import joblib


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "model.pkl"

model = joblib.load(MODEL_PATH)


def predict_price(data):
    features = [[
        data["longitude"],
        data["latitude"],
        data["housing_median_age"],
        data["population"],
        data["households"],
        data["median_income"]
    ]]

    prediction = model.predict(features)

    return prediction[0]