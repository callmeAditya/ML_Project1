from flask import Flask , request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

application = Flask(__name__)
app  = application



ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
       Temperature = float(request.form.get('Temperature'))
       RH = float(request.form.get('RH'))
       Ws = float(request.form.get('Ws'))
       Rain = float(request.form.get('Rain'))
       FFMC = float(request.form.get('FFMC'))
       DMC = float(request.form.get('DMC'))
       ISI = float(request.form.get('ISI'))
       Classes = float(request.form.get('Classes'))
       Region = float(request.form.get('Region'))
       
       new_scaled_data = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])    
       ridge_model_prediction = ridge_model.predict(new_scaled_data)
       
       print(ridge_model_prediction)
       
       return render_template('home.html', results=ridge_model_prediction[0])
       
       
    else:
        return render_template('home.html', results="get")


if __name__ == '__main__':
    app.run(host='0.0.0.0')