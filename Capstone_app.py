from flask import Flask, render_template, request
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib


le = LabelEncoder()

app = Flask(__name__)
model = joblib.load('RFC_model.joblib')
scaler_new = joblib.load('min_max_scaler.joblib')

@app.route('/')
def home():
    return render_template('capstone.html')


@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        CropDays = float(request.form['CropDays'])
        temperature = float(request.form['temperature'])
        SoilMoisture = float(request.form['SoilMoisture'])
        CropType = request.form['CropType']

        Crops = ['Wheat', 'Groundnuts', 'Garden Flowers', 'Maize', 'Paddy',
       'Potato', 'Pulse', 'Sugarcane', 'Coffee']
        
        CropsEncoded = [1 if CropType == k else 0 for k in Crops ]
        df2 = pd.DataFrame([CropsEncoded], columns=Crops)


        df1 = pd.DataFrame({'CropDays': [CropDays],'temperature': [temperature],
                                 'SoilMoisture': [SoilMoisture]})
        
        features = pd.concat([df1, df2], axis=1)
        features = scaler_new.transform(features)
        try:
            output = model.predict(features)

            prediction_text = "Prediction for loan amount is {}".format(output)

            return render_template('capstone.html', prediction_text=prediction_text)
        except ValueError as e:
            # Handle the ValueError here (e.g., provide a meaningful error message to the user)
            return "Error: {}".format(str(e))
            # Perform your prediction or processing here (not implemented in this example)
    else:
        # Display the initial form
        return render_template('capstone.html', prediction_text='')


if __name__ == '__main__':
    app.run(debug=True)


































