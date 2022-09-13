from django.forms import ModelForm
from django import forms
from .models import Location


class LocationForm(ModelForm):
    source_address = forms.CharField(max_length=100, required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Enter Pickup Address...'}))

    destination_address = forms.CharField(max_length=100, required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Enter Drop Address...'})) 
    
    class Meta:
        model = Location
        fields = '__all__'