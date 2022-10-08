from django import forms
from .models import HouseOwner, Houses


class HouseOwnerForm(forms.ModelForm):
    class Meta:
        model = HouseOwner
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


class HousesForm(forms.ModelForm):
    class Meta:
        model = Houses
        exclude = ('owner_name', 'is_available')
        labels = {
            'type': "",
            'bed_rooms': "",
            # 'category': "",
            'area': "",
            'doorno': "",
            'location': "",
            'city': "",
            'image1': "",
            'image2': "",
            'image3': "",
            'rent': "Enter Rent per month",
        }
        widgets = {
            'area': forms.TextInput(attrs={'placeholder': 'Enter Area in sq. mts.'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter Location'}),
            'doorno': forms.TextInput(attrs={'placeholder': 'Enter Door Number'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter City'}),
            'rent': forms.NumberInput(attrs={'placeholder': 'Enter Rent per month'}),
        }


