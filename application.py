from flask import Flask, request,jsonify,render_template
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
import pandas as pd

# import ridge regression and standard scaler pickle files
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))


application = Flask(__name__)
app=application

@app.route('/', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        #Get the data from the form
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        # Standardize the input data using the same scaler used for training
        scaled_data = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        # Predict using the loaded ridge regression model
        pred = ridge_model.predict(scaled_data)
        return render_template('index.html',result=round(pred[0],2))
    else:
        return render_template('index.html')
     
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    
    
