from fastapi import FastAPI
from pydantic import BaseModel

from app.model.model import predict_price


app = FastAPI(title="Car Price Prediction API")

# Mapping dictionaries to convert strings to numeric codes
name_mapping = {
    'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5,
    'Ford': 6, 'Renault': 7, 'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10,
    'Datsun': 11, 'Jeep': 12, 'Mercedes-Benz': 13, 'Mitsubishi': 14,
    'Audi': 15, 'Volkswagen': 16, 'BMW': 17, 'Nissan': 18, 'Lexus': 19,
    'Jaguar': 20, 'Land': 21, 'MG': 22, 'Volvo': 23, 'Daewoo': 24,
    'Kia': 25, 'Fiat': 26, 'Force': 27, 'Ambassador': 28, 'Ashok': 29,
    'Isuzu': 30, 'Opel': 31
}

fuel_mapping = {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4}

owner_mapping = {
    'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3,
    'Fourth & Above Owner': 4, 'Test Drive Car': 5
}

# Input model

class CarInput(BaseModel):
    name: str       # e.g., "Maruti"
    year: int
    km_driven: float
    fuel: str       # e.g., "Diesel"
    owner: str      # e.g., "First Owner"
    seats: int

@app.post("/predict")
def predict_car_price(data: CarInput):
    try:
        # Convert user-friendly strings to numeric codes
        features = [
            name_mapping[data.name],
            data.year,
            data.km_driven,
            fuel_mapping[data.fuel],
            owner_mapping[data.owner],
            data.seats
        ]
    except KeyError as e:
        return {"error": f"Invalid value: {e}. Please check input."}

    # Make prediction
    price = predict_price(features)

    # Format price nicely
    formatted_price = f"₦{round(price, 2):,.2f}"

    # Return full user-friendly JSON
    return {
        "Car": data.name,
       
        "Predicted Price": formatted_price
    }
