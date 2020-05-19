from django.conf.urls import url
from register import views

app_name = 'register'

urlpatterns = [
    url(r'^$', views.DeviceListView.as_view(),name='list'),
    

]
