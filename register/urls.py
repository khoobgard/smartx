from django.conf.urls import url
from register import views
from django.urls import path
app_name = 'register'

urlpatterns = [
    url(r'^$', views.DeviceListView.as_view(),name='list'),
    # url(r'^(?P<pk>[-\w]+)/$'), views.DeviceDetailView.as_view())
    path('<int:pk>/',views.DeviceDetailView.as_view()),
    url(r'^form/$',views.form_name_view,name='form_name')

]
