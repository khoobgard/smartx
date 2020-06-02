from django.contrib import admin
from register.models import Vehicle,Master,UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Vehicle)
admin.site.register(Master)
