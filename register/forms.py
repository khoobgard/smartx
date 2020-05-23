from django import forms
from register.models import Device,Master

class FormModelName(forms.ModelForm):
    class Meta():

        model = Device
        fields = '__all__'

class FormModelMaster(forms.ModelForm):
    class Meta():

        model = Master
        fields = '__all__'
