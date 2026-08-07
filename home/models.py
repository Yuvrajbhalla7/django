from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    image = models.ImageField(null=True)
    file = models.FileField(null=True)


  
class car(models.Model):
    car_name = models.CharField( max_length=50)
    speed = models.IntegerField(default=50)




