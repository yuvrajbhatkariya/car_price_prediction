from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the model (ensure the correct path to the model)
model_path = 'car2.pkl'
try:
    # Load the pre-trained model
    model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    print(f"Model file not found at {model_path}. Please check the path.")

# Encoding mappings for categorical features
brand_mapping = {
    'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5, 'Ford': 6,
    'Renault': 7, 'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10, 'Datsun': 11, 'Jeep': 12,
    'Mercedes-Benz': 13, 'Mitsubishi': 14, 'Audi': 15, 'Volkswagen': 16, 'BMW': 17,
    'Nissan': 18, 'Lexus': 19, 'Jaguar': 20, 'Land': 21, 'MG': 22, 'Volvo': 23,
    'Daewoo': 24, 'Kia': 25, 'Fiat': 26, 'Force': 27, 'Ambassador': 28, 'Ashok': 29,
    'Isuzu': 30, 'Opel': 31
}
fuel_mapping = {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4}
seller_type_mapping = {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3}
transmission_mapping = {'Manual': 1, 'Automatic': 2}
owner_mapping = {
    'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3,
    'Fourth & Above Owner': 4, 'Test Drive Car': 5
}

@app.route('index.html')
def home():
    return render_template('index.html')  # Updated to 'index.html'

@app.route('details.html')
def details():
    return render_template('details.html')

@app.route('reviews.html')
def reviews():
    return render_template('reviews.html')

@app.route('predict.html', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        brand = request.form['name']
        year = int(request.form['year'])
        km_driven = int(request.form['km_driven'])
        fuel = request.form['fuel']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']
        owner = request.form['owner']
        mileage = float(request.form['mileage'])
        engine = int(request.form['engine'])
        max_power = float(request.form['max_power'])
        seats = int(request.form['seats'])

        # Convert categorical data using encoding mappings
        brand_encoded = brand_mapping.get(brand, 0)
        fuel_encoded = fuel_mapping.get(fuel, 0)
        seller_type_encoded = seller_type_mapping.get(seller_type, 0)
        transmission_encoded = transmission_mapping.get(transmission, 0)
        owner_encoded = owner_mapping.get(owner, 0)

        # Prepare the input array for prediction
        input_data = np.array([[brand_encoded, year, km_driven, fuel_encoded, 
                                seller_type_encoded, transmission_encoded, owner_encoded, 
                                mileage, engine, max_power, seats]])

        # Perform prediction using the model
        predicted_price = model.predict(input_data)
        predicted_price = np.round(predicted_price[0], 2)

        # Format the result and pass it to the result page
        prediction_text = f"Predicted Car Price: ₹{predicted_price}"

        return render_template('result.html', prediction_text=prediction_text)

    except ValueError as e:
        return render_template('details.html', error_message="Error in prediction: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
