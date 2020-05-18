from django.shortcuts import render
from register.models import Device,Master
from django.views.generic import ListView,DetailViews
# Create your views here.
 class DeviceView(ListView):
     model = Device

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
