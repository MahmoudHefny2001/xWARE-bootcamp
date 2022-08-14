from django.db import models
from django import forms


# Create your models here.

class Task(models.Model):
    name = models.TextField(max_length=200)
