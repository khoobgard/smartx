from django import forms
from django.contrib.auth.models import User
from register.models import UserProfileInfo
from register.models import Device,Master


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pics')



class FormModelName(forms.ModelForm):
    class Meta():

        model = Device
        fields = '__all__'

class FormModelMaster(forms.ModelForm):
    class Meta():

        model = Master
        fields = '__all__'
