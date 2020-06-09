from django import forms
from django.contrib.auth.models import User
from register.models import UserProfileInfo
from vehicles.models import Vehicle,Master
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Invisible


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

#     captcha = ReCaptchaField(
#     public_key='6Ldou_0UAAAAANymj1RdQ7VqZy97FLslCAI02aCU',
#     private_key='6Ldou_0UAAAAAAFPVYs7nl3FEL5op63LtTm-W3y_',
# )
#     captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pics')
