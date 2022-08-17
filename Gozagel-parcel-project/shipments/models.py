
from re import A
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
    # shipment_id = models.CharField(max_length=100)
    # shipment_reference = models.CharField(max_length=100, null=True, blank=True)
    # user = models.OneToOneField(get_user_model(), on_delete=RESTRICT)
    # shipper = models.ForeignKey(Address, related_name='shipper', on_delete=models.CASCADE)
    # recipient = models.ForeignKey(Address, related_name='recipient', on_delete=models.CASCADE)
    shipment_id = models.CharField(max_length=255, null=True, blank=True)
    shipper_id = models.CharField(max_length=255, null=True, blank=True)
    recipient_id = models.CharField(max_length=255, null=True, blank=True)
    parcel_id = models.CharField(max_length=255, null=True, blank=True)
    items_id = models.CharField(max_length=255, null=True, blank=True)
    customs_id = models.CharField(max_length=255, null=True, blank=True)
    commodities_id = models.CharField(max_length=255, null=True, blank=True)
    # parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE, null=True, blank=True)
    # item = models.ForeignKey(Items, on_delete=models.CASCADE, null=True, blank=True)
    # reference = models.CharField(max_length=100, null=True, blank=True)
    # label_type = models.CharField(max_length=50, default="PDF", null=True, blank=True)
    # service = models.CharField(max_length=50, null=True, blank=True)
    # services = ArrayField(models.CharField(max_length=10, blank=True, null=True))
    # carrier_ids = ArrayField(models.CharField(max_length=10, blank=True),)






    















