from django.db import models

# Create your models here.
class Master(models.Model):
    name = models.CharField(max_length=200)
    type = models.Choices({'r':'raspberry','a':'arduino'})
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=200)
    type = models.Choices()
    code = models.IntegerField(unique=True)
    master = models.ForeignKey(Master,on_delete=models.CASCADE)

    def __str__(self):
        
