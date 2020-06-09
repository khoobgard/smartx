from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from vehicles.models import Vehicle

# Create your views here.
def index(request):
    return render(request,'register/index.html')

class Rent(View):
    
    @login_required
    def rent_request(self,request):
        form_rent = forms.FormModelRent()
        if request.method == 'POST' and form_rent.is_valid:
            form_rent = forms.FormModelRent(request.POST)
            bike_code = request.POST["code"]

            bike = Vehicle.objects.all().filter(code=bike_code)
            my_bike_status = bike.status

            if bike.status == 'r':
                bike.status = 's'
                bike.save()

                return render(request,'register/dashboard.html',
                    context={"bike":bike_code,"status":my_bike_status,'time':timezone.now })


        else:
                print('ERROR')

        return render(request,'register/rent_vehicle.html',{'form_rent': form_rent})


    @login_required
    def rent_pause(self,request):
        if my_bike.status == 's':
            my_bike.status = 'b'
            my_bike.save()


    @login_required
    def rent_finish(self,request):
        pass
