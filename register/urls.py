from django.conf.urls import url
from register import views
from django.urls import path

app_name = 'register'

urlpatterns = [
    url(r'^$', views.DeviceListView.as_view(),name='list'),
    # url(r'^(?P<pk>[-\w]+)/$'), views.DeviceDetailView.as_view())
    path('list/<int:pk>/',views.DeviceDetailView.as_view()),
    url(r'^device/$',views.form_device_view,name='form_device'),
    url(r'^master/$',views.form_master_view,name='form_master'),
    url(r'^register/$',views.register,name='registration'),




]
