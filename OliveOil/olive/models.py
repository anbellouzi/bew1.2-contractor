import datetime
from django import forms
from django.db import models
from django.utils import timezone

class OliveOil(models.Model):
    olive_name = models.CharField(max_length=200)
    olive_description = models.CharField(max_length=200)
    olive_image = models.CharField(max_length=200)
    olive_price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.olive_name


class Order(models.Model):
    # product =  models.ForeignKey(OliveOil, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_number = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name
