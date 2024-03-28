# 1. Library imports
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

#. Load trained Pipeline
model = load_model('House-sales-10pred-tuned')

# Define predict function
@app.post('/predict')
def predict(lat, long, sqft_living, sqft_above, sqft_living15, sqft_lot15, yr_built, zipcode, sqft_basement, grade):
    data = pd.DataFrame([[lat, long, sqft_living, sqft_above, sqft_living15, sqft_lot15, yr_built, zipcode, sqft_basement, grade]])
    data.columns = ["lat", "long", "sqft_living", "sqft_above", "sqft_living15", "sqft_lot15", "yr_built", "zipcode", "sqft_basement", "grade"]
    predictions = predict_model(model, data=data) 
    return {
        "lat" : float(predictions['lat'][0]),
        "long" : float(predictions['long'][0]),
        "sqft_living" : int(predictions['sqft_living'][0]),
        "sqft_above" : int(predictions['sqft_above'][0]),
        "sqft_living15" : int(predictions['sqft_living15'][0]),
        "sqft_lot15" : int(predictions['sqft_lot15'][0]),
        "sqft_basement" : int(predictions['sqft_basement'][0]),
        "yr_built" : int(predictions['yr_built'][0]),
        "zipcode" : int(predictions['zipcode'][0]),
        "grade" : int(predictions['grade'][0]),
        "price": int(predictions['prediction_label'][0])}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=1234)

