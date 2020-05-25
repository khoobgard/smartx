from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=None)

    portfolio_site = models.URLField(blank= True)
    profile_pic = models.ImageField(upload_to= 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class Master(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=300)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=300)
    code = models.IntegerField(unique=True)
    master = models.ForeignKey(Master,related_name='device',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
