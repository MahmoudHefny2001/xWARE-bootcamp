from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.BigIntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200) 
    email = models.EmailField()
    image = models.ImageField()

class studentLinks(models.Model):
    facebook = models.CharField()
    instagram = models.CharField()
    twitter = models.CharField()
   