import requests

def get_predictions(lat, long, sqft_living, sqft_above, sqft_living15, sqft_lot15, yr_built, zipcode, sqft_basement, grade):
    url = 'http://prediction:1234/predict?lat={lat}&long={long}&sqft_living={sqft_living}&sqft_above={sqft_above}&sqft_living15={sqft_living15}&sqft_lot15={sqft_lot15}&yr_built={yr_built}&zipcode={zipcode}&sqft_basement={sqft_basement}&grade={grade}'.format(lat=lat, long=long, sqft_living=sqft_living, sqft_above=sqft_above, sqft_living15=sqft_living15, sqft_lot15=sqft_lot15, zipcode=zipcode, yr_built=yr_built, sqft_basement=sqft_basement, grade=grade)
    x = requests.post(url).json()
    return x