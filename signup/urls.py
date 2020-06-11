from django.conf.urls import url
from signup import views
from django.urls import path

app_name = 'signup'

urlpatterns = [
    url(r'^$', views.VehicleListView.as_view(),name='list'),
    # url(r'^(?P<pk>[-\w]+)/$'), views.DeviceDetailView.as_view())
    path('<int:pk>',views.VehicleDetailView.as_view()),
    url(r'^vehicle/$',views.form_vehicle_view,name='form_vehicle'),
    url(r'^master/$',views.form_master_view,name='form_master'),
    url(r'^signup/$',views.signup,name='registered'),


]
