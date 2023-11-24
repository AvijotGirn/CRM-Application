from django.db import models


# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
