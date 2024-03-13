
# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_selection, name='car_selection'),
]
