from django.shortcuts import render
from register.models import Vehicle
from django.views.generic import TemplateView,ListView,DetailView
from django.utils import timezone
from register import forms

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class VehicleListView(ListView):
    context_object_name = 'vehicles'
    model = Vehicle
    template_name = 'register/vehicle_list.html'


class VehicleDetailView(DetailView):
    context_object_name = 'vehicle_detail'
    model = Vehicle
    template_name = 'register/vehicle_detail.html'

def index(request):
    my_vehicle = Vehicle.objects.get(name='bike2')
    return render(request,'register/index.html',context={"vehicle":my_vehicle})

@login_required
def form_rent_view(request):
    form_rent = forms.FormModelRent()
    if request.method == 'POST':
        form_rent = forms.FormModelRent(request.POST)

        if form_rent.is_valid:
            your_bike = request.POST["code"]

            my_bike = Vehicle.objects.get(code=int(your_bike))

            if my_bike.status == 'r':
                my_bike.status = 's'
                my_bike.save()

                return render(request,'register/dashboard.html',
                        context={"myvehicle":my_bike,'time':timezone.now })
            else:
                return render(request,'register/index.html',
                        context={"bike":my_bike,"message":"is not in service"})


        else:
            print('ERROR')

    return render(request,'register/rent_vehicle.html',{'form': form_rent})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES.get('profile_pics')

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'register/registration.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})



# LOGIN
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'),{'user':username})
            else:
                HttpResponse("account not active")

        else:
            print("someone tried to login but failed")
            print("username : {} , password : {} ".format(username,password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request,'register/login.html')





def form_vehicle_view(request):
    form = forms.FormModelName()
    if request.method == 'POST':
        form = forms.FormModelName(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR')

    return render(request,'register/form_vehicle.html',{'form': form})


def form_master_view(request):
    form1 = forms.FormModelMaster()
    if request.method == 'POST':
        form1 = forms.FormModelMaster(request.POST)

        if form1.is_valid:
            form1.save(commit=True)
            return index(request)
        else:
            print('ERROR')

    return render(request,'register/form_master.html',{'form1': form1})
