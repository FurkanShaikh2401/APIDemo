import imp
from django.urls import path
from . import views


urlpatterns = [
    path('', views.AddressBooking, name="home"),
    path('show/', views.BookingDetails, name="details"),
]
