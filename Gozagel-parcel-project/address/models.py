from django.db import models

# Create your models here.

class Address(models.Model):
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    federal_tax_id = models.CharField(max_length=50)
    state_tax_id = models.CharField(max_length=50)
    person_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=2, default="AD")
    email = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    state_code = models.CharField(max_length=20)
    suburb = models.CharField(max_length=255)
    residential = models.BooleanField(default=False)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    validate_location = models.BooleanField(default=False)
