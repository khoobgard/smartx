from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from vehicles.models import Vehicle
from rent import views
from signup.forms import UserForm
from rent import forms
from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request,'signup/index.html')



@login_required
def rent_request(request):
    form_rent = forms.FormModelRent()
    if request.method == 'POST' and form_rent.is_valid:
        form_rent = forms.FormModelRent(request.POST)
        bike_code = request.POST["code"]

        bike = Vehicle.objects.all().filter(code=bike_code)
        my_bike_status = bike.status

        if bike.status == 'r':
            bike.status = 's'
            bike.save()

        return render(request,'signup/dashboard.html',
                    context={"bike":bike_code,"status":my_bike_status,'time':'now' })


    else:
        print('ERROR')

    return render(request,'rent/rent_vehicle.html',{'form_rent': form_rent})


@login_required
def rent_pause(request):
    if my_bike.status == 's':
        my_bike.status = 'b'
        my_bike.save()


@login_required
def rent_finish(request):
    pass
