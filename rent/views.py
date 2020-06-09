from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
class Rent():

@login_required
def rent_request(request):
    form_rent = forms.FormModelRent()
    if request.method == 'POST' and form_rent.is_valid:
        form_rent = forms.FormModelRent(request.POST)

        your_bike = request.POST["code"]


        return render(request,'register/dashboard.html',
                context={"bike":my_bike,"status":my_bike_status,'time':timezone.now })


        
    else:
            print('ERROR')

    return render(request,'register/rent_vehicle.html',{'form': form_rent})

def rent_pause(request):
    if my_bike.status == 's':
        my_bike.status = 'b'
        my_bike.save()

def rent_finish(request):
    pass
