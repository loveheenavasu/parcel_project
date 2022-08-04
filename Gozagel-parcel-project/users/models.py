from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def get_name(self):
        return self.name


class Addresses(models.Model):
    person_name = models.CharField(
        "Full name",
        max_length=1024,
    )
    address_line1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )
    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )
    postal_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )
    city = models.CharField(
        "City",
        max_length=1024,
    )
    country_code = models.CharField(
        "Country code",
        max_length=40,
    )


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    apartment_suit = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal = models.IntegerField()

    def get_vat_number(self):
        return self.name
