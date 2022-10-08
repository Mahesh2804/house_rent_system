from django.core import validators
from django.db import models
from django.core.validators import *

# Create your models here.

class HouseCustomer(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = ( ('Male','MALE'), ('Female','FEMALE') )
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    username = models.CharField(max_length=100, blank=False, primary_key=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=6)])
    mobileno = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    city = models.CharField(max_length=100, blank=False)
    
    class Meta:
        db_table = "housecustomer_table"


class Orders(models.Model):
    customer_name = models.CharField(max_length=100, blank=False)
    house_type = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=200, blank=False)
    area = models.IntegerField(blank=False)
    bedrooms = models.CharField(max_length=10, blank=False)
    owner_name = models.CharField(max_length=100, blank=False)
    owner_mobile = models.CharField(max_length=12, blank=False, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    rent = models.DecimalField(decimal_places=2, max_digits=65, blank=False)
    
    class Meta:
        db_table = "houses_orders"

