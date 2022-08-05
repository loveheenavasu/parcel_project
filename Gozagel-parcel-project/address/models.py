from tkinter.tix import Balloon
from django.db import models

# Create your models here.

class Address(models.Model):
    postal_code = models.CharField(max_length=10, null=True,blank=True)
    city = models.CharField(max_length=50, null=True,blank=True)
    federal_tax_id = models.CharField(max_length=50, null=True,blank=True)
    state_tax_id = models.CharField(max_length=50, null=True,blank=True)
    person_name = models.CharField(max_length=50, null=True,blank=True)
    company_name = models.CharField(max_length=50, null=True,blank=True)
    country_code = models.CharField(max_length=2, default="AD")
    email = models.CharField(max_length=255, null=True,blank=True)
    phone_number = models.CharField(max_length=50, null=True,blank=True)
    state_code = models.CharField(max_length=20, null=True,blank=True)
    suburb = models.CharField(max_length=255, null=True,blank=True)
    residential = models.BooleanField(default=False, null=True,blank=True)
    address_line1 = models.CharField(max_length=100, null=True,blank=True)
    address_line2 = models.CharField(max_length=100, null=True,blank=True)
    validate_location = models.BooleanField(default=False)
