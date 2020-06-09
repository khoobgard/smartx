from django.contrib import admin
from vehicles.models import Vehicle,Master
from signup.models import UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Vehicle)
admin.site.register(Master)
