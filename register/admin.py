from django.contrib import admin
from register.models import Device,Master,UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Device)
admin.site.register(Master)
