import joblib
import numpy as np

# Load the trained model
model = joblib.load("app/model/car_price_model.pkl")


# Define a prediction function


def predict_price(features: list):
    """
    features: list of numeric values in the same order as model input
    Example: [year, km_driven, fuel, owner, seats]
    """
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)
    return prediction[0]
