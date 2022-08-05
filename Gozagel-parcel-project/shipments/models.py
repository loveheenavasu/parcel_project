
from django.db import models
from parcels.models import Items, Parcel
from address.models import Address
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import RESTRICT
from django.contrib.auth import get_user_model




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
    shipment_id = models.CharField(unique=True, max_length=100)
    shpment_reference = models.CharField(unique=True, max_length=100)
    user = models.OneToOneField(get_user_model(), on_delete=RESTRICT)
    shipper = models.ForeignKey(Address,related_name='shipper', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Address,related_name='recipient', on_delete=models.CASCADE)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    reference = models.CharField(max_length=100, null=True, blank=True)
    label_type = models.CharField(max_length=50, default="PDF")
    service = models.CharField(max_length=50)
    services = ArrayField(models.CharField(max_length=10, blank=True),)
    carrier_ids = ArrayField(models.CharField(max_length=10, blank=True),)






    















