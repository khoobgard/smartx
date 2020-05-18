from django.conf.urls import url
from register.views import DeviceView

urlpatterns = [
    url(r'^devices/', DeviceView.as_view()),

]
