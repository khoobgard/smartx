from django.conf.urls import url
from rent import views
from django.urls import path

app_name = 'rent'

urlpatterns = [
    url(r'^request$', views.Rent.rent_request.as_view(),name='rent_request'),
    url(r'^pause$', views.Rent.rent_pause.as_view(),name='rent_pause'),
    url(r'^pause$', views.Rent.rent_finish.as_view(),name='rent_finish'),


]
