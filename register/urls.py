from django.conf.urls import url
from register import views

urlpatterns = [
    url(r'^devices/', views.DeviceView.as_view()),

]
