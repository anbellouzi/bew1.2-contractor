from django.db import models
from django.utils import timezone
import datetime


class Sauce(models.Model):
    sauce_name = models.CharField(max_length=200)
    sauce_description = models.CharField(max_length=200)
    sauce_price = models.IntegerField(default=0)
    sauce_rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sauce_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Order(models.Model):
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    sale_price = models.IntegerField(default=0)

    def __str__(self):
        return self.customer_name
