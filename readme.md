# Forest Fire Predictor

This project predicts the Fire Weather Index (FWI) using weather-related features from a dataset sourced on Kaggle.  
It is built using Flask and deployed on AWS.

## About The Project

Using historical weather data, this machine learning model predicts FWI, which indicates the likelihood of forest fire danger.  
The focus of this project is on regression modeling and deploying the model through a simple web app.

## Data Source

- Dataset from Kaggle containing fire-related data for two regions in Algeria.
- Includes temperature, humidity, wind speed, and other meteorological variables.

## Exploratory Data Analysis (EDA)

Conducted EDA to understand:
- Distribution of fire occurrences
- Feature importance
- Weather influence on FWI

## Model Building

Regression models used:
- Linear Regression
- Lasso Regression
- Ridge Regression
- Random Forest Regressor

## Model Selection

- R² Score used to evaluate regression models
- Hyperparameter tuning with RandomizedSearchCV
- Cross-validation used to validate model performance

## Flask App

- Built using Flask framework
- Provides a simple UI to input values and get predictions
- `/predict_api` route available for testing via tools like Postman

## AWS Deployment

- App deployed on AWS EC2 instance
- Dependencies installed on the instance
- Flask app served and made accessible via public IP

## Technologies Used

- Python
- Flask
- scikit-learn
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Tools Used

- Git
- AWS EC2
- Postman
- VS Code

