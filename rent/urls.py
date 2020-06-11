from django.conf.urls import url
from rent import views
from django.urls import path

app_name = 'rent'

urlpatterns = [
    path('', views.rent_request,name='rent_request'),
    path('pause', views.rent_pause,name='rent_pause'),
    path('pause', views.rent_finish,name='rent_finish'),

]
