from django.core import validators
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *

# Create your models here.

class HouseOwner(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = ( ('Male','MALE') , ('Female','FEMALE')  )
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    username = models.CharField(max_length=100, blank=False, primary_key=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=6)])
    mobileno = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=10)])
    city = models.CharField(max_length=100, blank=False)
    
    class Meta:
        db_table = "houseowner_table"


class Houses(models.Model):
    owner_name = models.CharField(max_length=100,blank=False)
    type_choices = (('default','Select Type'),('Apartment Flat','APARTMENT FLAT'), ('Bungalow','BUNGALOW'), ('Villa','VILLA'), ('Duplex','DUPLEX'), ('Others','OTHERS'))
    type = models.CharField(max_length=100,blank=False,choices=type_choices,default='default')
    bedroom_choices = (('default','No.of Bedrooms'),('1','1'),('2','2'),('3','3'))
    bed_rooms = models.CharField(max_length=100,blank=False,choices=bedroom_choices,default='default')
    image1 = models.ImageField(upload_to='static/images/houses/')
    image2 = models.ImageField(upload_to='static/images/houses/')
    image3 = models.ImageField(upload_to='static/images/houses/')
    area = models.IntegerField(blank=False)
    doorno = models.CharField(max_length=200,blank=False,primary_key=True)
    location = models.CharField(max_length=200,blank=False)
    city = models.CharField(max_length=100,blank=False)
    rent = models.DecimalField(decimal_places=2, max_digits=65, default=9000)
    is_available = models.BooleanField(default = True)

    
    class Meta:
        db_table = "owner_houses"