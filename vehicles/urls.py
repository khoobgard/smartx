from django.conf.urls import url
from vehicles import views
from django.urls import path

app_name = 'vehicles'

urlpatterns = [
    url(r'^$', views.VehicleListView.as_view(),name='list'),
    path('<int:pk>',views.VehicleDetailView.as_view()),
    url(r'^vehicle/$',views.form_vehicle_view,name='form_vehicle'),
    url(r'^master/$',views.form_master_view,name='form_master'),

]
