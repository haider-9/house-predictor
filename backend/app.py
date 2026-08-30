from flask import Flask, request, jsonify
from services.predictor import predict_price

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    price = predict_price(data)

    return jsonify({
        "predicted_price": price
    })


if __name__ == "__main__":
    app.run(debug=True)