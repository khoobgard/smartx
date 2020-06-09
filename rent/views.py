from django.shortcuts import render

# Create your views here.

@login_required
def form_rent_view(request):
    form_rent = forms.FormModelRent()
    if request.method == 'POST':
        form_rent = forms.FormModelRent(request.POST)

        if form_rent.is_valid:
            your_bike = request.POST["code"]

            my_bike = Vehicle.objects.get(code=int(your_bike))
            my_bike_status = my_bike.status

            if my_bike.status == 'r':
                my_bike.status = 's'
                my_bike.save()

                return render(request,'register/dashboard.html',
                context={"bike":my_bike,"status":my_bike_status,'time':timezone.now })

            elif my_bike.status == 's':
                my_bike.status = 'b'
                my_bike.save()

            return render(request,'register/dashboard.html',
                            context={"bike":my_bike,"status":my_bike_status,'time':timezone.now })
        else:
                    return render(request,'register/dashboard.html',
                            context={"bike":my_bike,"status":my_bike_status,"message":"is not in service"})


    else:
            print('ERROR')

    return render(request,'register/rent_vehicle.html',{'form': form_rent})
