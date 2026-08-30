from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
from utils.preprocessing import load_data

X_train, X_test, y_train, y_test = load_data()

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("R² Score:", r2)

joblib.dump(model, "models/model.pkl")

print("Model trained and saved successfully.")