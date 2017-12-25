from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=75)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    sex = models.CharField(max_length=1)


class zakaz(models.Model):
    name = models.CharField(max_length=30)
    Usluga = models.CharField(max_length=255, null=True)
    #price = models.FloatField(max_length=10)

    objects = models.Manager()


class Usluga(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user_zakaz = models.ForeignKey(zakaz, on_delete=models.CASCADE)
    date = models.DateField()
