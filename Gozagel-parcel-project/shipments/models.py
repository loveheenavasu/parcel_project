from email.headerregistry import Address
from mmap import MADV_AUTOSYNC
from pyexpat import model
from re import M, T
from statistics import mode
from tkinter import CASCADE
from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import FieldDoesNotExist
from django.db.models.deletion import RESTRICT
from numpy import MachAr
from customs.models import Bill_to, Commodities, Duty, Other
from parcels.models import Items, Parcel
from address.models import Address
from django.contrib.postgres.fields import ArrayField


class Options(models.Model):
    aes = models.CharField(max_length=255)
    eel_pfc = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=255)
    nip_number = models.CharField(max_length=255)
    eori_number = models.CharField(max_length=255)
    vat_registration_number = models.CharField(max_length=255)

class selected_rate(models.Model):
    object_type = models.CharField(max_length=200)
    carrier_name = models.CharField(max_length=200)
    carrier_id = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    total_charge = models.CharField(max_length=20)
    transit_days = models.CharField(max_length=20)
    extra_charges = models.CharField(max_length=50)
    

class Shipments(models.Model):
    # shipment_id = models.CharField(unique=True, max_length=100)
    # shpment_reference = models.CharField(unique=True, max_length=100)
    # user = models.OneToOneField(get_user_model(), on_delete=RESTRICT)
    
    shipper = models.ForeignKey(Address, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Address, on_delete=models.CASCADE)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    options = models.ForeignKey(Options, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    options = models.ForeignKey(options, on_delete=CASCADE, default={})
    reference = models.CharField(max_length=100, null=True, blank=True)
    label_type = models.CharField(max_length=50, default="PDF")
    service = models.CharField(max_length=50)
    services = ArrayField(models.CharField(max_length=10, blank=True),)
    carrier_ids = ArrayField(models.CharField(max_length=10, blank=True),)






    















