from django.shortcuts import render
from register.models import Device
from django.views.generic import TemplateView,ListView,DetailView
from django.utils import timezone
from register import forms
# Create your views here.

# class DeviceView(TemplateView):
#     template_name='register/device_list.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context = {'inject':timezone.now(),'majid':'salam'}
#         return context

class DeviceListView(ListView):
    context_object_name = 'devices'
    model = Device
    template_name = 'register/device_list.html'

class DeviceDetailView(DetailView):
    context_object_name = 'device_detail'
    model = Device
    template_name = 'register/device_detail.html'

def Index(request):
    return render(request,'register/index.html')


def form_name_view(request):
    form = forms.FormModelName()
    if request.method == 'POST':
        form = forms.FormModelName(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return Index(request)
        else:
            print('ERROR')

    return render(request,'register/device_list.html',{'form': form})
