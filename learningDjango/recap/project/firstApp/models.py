from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=15, null=False, unique=True)
    email = models.EmailField(max_length=110, unique=True)


class ContactUserInfo(models.Model):
    contact = models.ForeignKey(ContactModel, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=200, null=True)


