from django.db import models

# Create your models here.

class ContactUs(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=False)
    phone = models.BigIntegerField(blank=False)
    message = models.TextField(blank=False)

    class Meta:
        db_table = "usermessages_table"