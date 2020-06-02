from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=None)

    portfolio_site = models.URLField(blank= True)
    profile_pics = models.ImageField(upload_to= 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class Master(models.Model):
    name = models.CharField(max_length=200)
    master_type = (('pi3','raspberry pi 3'),
                ('pi4','raspberry pi 4'),
                ('zerow','raspberry pi zer w'),
                )
    type = models.CharField(choices=master_type , max_length=10)
    code = models.IntegerField(unique=True)
    power_type = (('3.3','voltage 3.3'),
            ('5','voltage 5'),
            ('12','voltage 12'),
            )
    power = models.CharField(choices=power_type , max_length=3,default='5')

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    model = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=300)
    code = models.IntegerField(unique=True)
    master = models.ForeignKey(Master,related_name='vehicle',
                                on_delete=models.CASCADE)

    status_mode = (('o','out of service'),
                    ('s','in service'),
                    ('r','ready to service'),
                    ('b','standby'),
                    )
    status = models.CharField(choices=status_mode , max_length=1)



    def __str__(self):
        return self.name
