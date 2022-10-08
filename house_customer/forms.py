from django import forms
from django.forms import widgets
from .models import HouseCustomer
from django.db import models

class HouseCustomerForm(forms.ModelForm):
    class Meta:
        model = HouseCustomer
        fields = "__all__"
        labels = {
            'fullname': "",
            'username': "",
            'password': "",
            'gender': "Select Gender",
            'email': "",
            'mobileno': "",
            'city': "",
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Enter FullName'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter UserName'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
            'mobileno': forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter City'}),
        }


class SearchForm(forms.Form):
    type_choices = [('default', 'Select Type'), ('Apartment Flat','APARTMENT FLAT'), ('Bungalow','BUNGALOW'), ('Villa','VILLA'), ('Duplex','DUPLEX'), ('Others','OTHERS')]
    type = forms.ChoiceField(choices=type_choices, label='')
    category_choices = [('default', 'Select Category'), ('For Sale','For Sale'),('For Rent','For Rent')]
    category = forms.CharField(required=True, label='', widget=forms.Select(choices=category_choices, attrs={"placeholder": "Select Category"}))
    bedroom_choices = [('default', 'No.of Bedrooms'), ('1','1'),('2','2'),('3','3')]
    bed_rooms = forms.CharField(required=True, label='', widget=forms.Select(choices=bedroom_choices, attrs={"placeholder": "No.of Bedrooms" }))
    city = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={"placeholder": "City"}))
