from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prediction/', views.prediction, name='prediction'),
    path('show_price/<str:lat>/<str:long>/<str:sqft_living>/<str:sqft_above>/<str:sqft_living15>/<str:sqft_lot15>/<str:yr_built>/<str:zipcode>/<str:sqft_basement>/<str:grade>', views.show_price, name='show_price'),
    path('dashboard/', views.show_dashboard, name='dashboard')
]