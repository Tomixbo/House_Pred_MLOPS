from django.shortcuts import render
from django.urls import reverse
from .prediction import get_predictions
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'prediction/index.html')

def prediction(request):
    
    if request.method == 'POST':
        lat = request.POST.get("lat")
        long = request.POST.get("long")
        yr_built = request.POST.get("yr_built")
        zipcode = request.POST.get("zipcode")
        sqft_living = request.POST.get("sqft_living")
        sqft_above = request.POST.get("sqft_above")
        sqft_living15 = request.POST.get("sqft_living15")
        sqft_lot15 = request.POST.get("sqft_lot15")
        sqft_basement = request.POST.get("sqft_basement")
        grade = request.POST.get("grade")
        return HttpResponseRedirect(reverse('show_price', args=[lat, long, sqft_living, sqft_above, sqft_living15, sqft_lot15, yr_built, zipcode, sqft_basement, grade]))

    return render(request, 'prediction/prediction.html')

def show_price(request, lat, long, sqft_living, sqft_above, sqft_living15, sqft_lot15, yr_built, zipcode, sqft_basement, grade):
    predictions=get_predictions(float(lat), float(long), int(sqft_living), int(sqft_above), int(sqft_living15), int(sqft_lot15), int(yr_built), int(zipcode), int(sqft_basement), int(grade))
    context = {
        'lat' : predictions['lat'],
        'long' : predictions['long'],
        'sqft_living' : predictions['sqft_living'],
        'sqft_above' : predictions['sqft_above'],
        'sqft_living15' : predictions['sqft_living15'],
        'sqft_lot15' : predictions['sqft_lot15'],
        'sqft_basement' : predictions['sqft_basement'],
        'yr_built' : predictions['yr_built'],
        'zipcode' : predictions['zipcode'],
        'grade' : predictions['grade'],
        'price': predictions['price']
    }
    return render(request, 'prediction/show_price.html', context)


def show_dashboard(request):
    return render(request, 'prediction/dashboard.html')