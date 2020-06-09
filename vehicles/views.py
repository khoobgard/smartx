from django.shortcuts import render
from vehicles.models import Vehicle
from django.views.generic import TemplateView,ListView,DetailView
from django.utils import timezone
from vehicles import forms

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
