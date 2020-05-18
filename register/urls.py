from django.conf.urls import url
from register.views import DeviceView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^devices/', DeviceView.as_view()),

]
