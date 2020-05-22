from django import forms
from register.models import Device

class FormModelName(forms.ModelForm):
    class Meta:

        model = Device
        fields = '__all__'
