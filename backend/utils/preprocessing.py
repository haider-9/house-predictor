from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
BASE_DIR = Path(__file__).resolve().parent

csv_path = BASE_DIR / "data" / "data.csv"

df = pd.read_csv(csv_path)
def load_date():
    X = df[["longitude", "latitude", "housing_median_age","population", "households", "median_income"]]
    y = df["median_house_value"]

    X_train, X_test, y_train, y_test=train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,)