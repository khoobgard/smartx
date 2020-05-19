from django.shortcuts import render
from register.models import Device
from django.views.generic import TemplateView
from django.utils import timezone
# Create your views here.

class DeviceView(TemplateView):
    template_name='register/device_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context = {'inject':timezone.now(),'majid':'salam'}
        return context

# class DeviceListView(ListView):
#      model = Device
#      template_name='register/device_list.html'
#      context_object_name='device_list'
