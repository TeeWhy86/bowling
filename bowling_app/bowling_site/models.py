from django.db import models

# Create your models here.


class Customer(models.Model):
    first = models.CharField(max_length=60)
    middle = models.CharField(max_length=60)
    last = models.CharField(max_length=60)
    birthdate = models.DateField()
    gender = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    zipcode = models.IntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.CharField(max_length=255)