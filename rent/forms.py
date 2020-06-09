from django import forms
from vehicles.models import Vehicle

class FormModelRent(forms.ModelForm):
    class Meta():

        model = Vehicle
        fields = ['code']
