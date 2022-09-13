from django.shortcuts import render, redirect
from .models import Location
from .forms import LocationForm
from django.conf import settings

# Create your views here.


def AddressBooking(request):
    location_form = LocationForm()

    if request.method == 'POST':
        location_form = LocationForm(request.POST)

        if location_form.is_valid():
            location_form.save()
            return redirect('show')
            
    context = {'form': location_form, 'google_api_key': settings.GOOGLE_API_KEY}
    return render(request, 'AddressForm.html', context)

def BookingDetails(request):
    
    return render(request, 'showBookingDetails.html', {})
