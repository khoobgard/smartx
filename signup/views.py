from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.utils import timezone
from signup import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'signup/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
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

        elif 'profile_pics' in request.FILES:
            profile.profile_pics = request.FILES.get('profile_pics')

            profile.save()

            registered = True
        else:

            print(user_form.errors,profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

        return render(request, 'signup/registration.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})



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
        return render(request,'signup/login.html')
