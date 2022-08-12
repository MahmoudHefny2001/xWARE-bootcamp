from django.db import models

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=200)
    age = models.BigIntegerField()
    salary = models.BigIntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200) 
    email = models.EmailField()
    image = models.ImageField()

