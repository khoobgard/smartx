from django.conf.urls import url
from rent import views
from django.urls import path

app_name = 'register'

urlpatterns = [
    url(r'^$', views.VehicleListView.as_view(),name='list'),
    path('<int:pk>',views.VehicleDetailView.as_view()),


]
