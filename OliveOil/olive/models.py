import datetime
from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class OliveOil(models.Model):
    olive_name = models.CharField(max_length=200)
    olive_description = models.CharField(max_length=200)
    olive_image = models.CharField(max_length=200)
    olive_price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.olive_name


class Order(models.Model):
    author =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    olive_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    Zip_code = models.IntegerField(null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


    def __str__(self):
        return self.full_name
