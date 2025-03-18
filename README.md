# ML_Project1
# Flask Application for Predicting Data Points

## Overview
This Flask-based web application predicts outcomes using a Ridge Regression model. The app processes user-input data, applies standard scaling, and feeds it into a pre-trained model to generate predictions.

## Features
- Web-based UI for user input
- Flask-based backend
- Machine Learning model integration using `pickle`
- Preprocessing with `StandardScaler`
- Predictive results displayed on the UI

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- NumPy
- Pandas
- scikit-learn
- Pickle

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure
```
/
├── models/
│   ├── ridge.pkl          # Pre-trained Ridge Regression model
│   ├── scaler.pkl         # StandardScaler object for data normalization
│
├── templates/
│   ├── index.html         # Landing page
│   ├── home.html          # Prediction result page
│
├── app.py                 # Main application script
├── requirements.txt       # Dependencies list
└── README.md              # Documentation
```

## Running the Application
1. Ensure `models/ridge.pkl` and `models/scaler.pkl` exist.
2. Start the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter the required input values (Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region).
2. Submit the form.
3. View the predicted result on the webpage.

## Deployment
To deploy on a cloud server, use:
```bash
flask run --host=0.0.0.0 --port=5000
```
You can also containerize the app using Docker or deploy it on platforms like AWS, Heroku, or Render.

## License
This project is licensed under the MIT License.

