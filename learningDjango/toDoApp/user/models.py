from django.db import models
from distutils.command.upload import upload
from django import forms
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)


class Tasks(models.Model):
    name = models.CharField(max_length=200)