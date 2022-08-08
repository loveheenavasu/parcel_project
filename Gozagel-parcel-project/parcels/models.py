"""
PARCEL api models
"""
from django.db import models
# from django.forms import CharField


# Create your models here.
class Items_metadata(models.Model):
    """
    TODO: how many references are required 
    """
    part_number= models.CharField(max_length=255, null=True, blank=True)
    reference1= models.CharField(max_length=255, null=True, blank=True)
    reference2= models.CharField(max_length=255, null=True, blank=True)
    reference3= models.CharField(max_length=255, null=True, blank=True)
    reference4= models.CharField(max_length=255, null=True, blank=True)

class Items(models.Model):
    """
    Models to create the Items in the Parcel API
    """
    items_id = models.CharField(max_length=255, null=True, blank=True)
    weight = models.IntegerField()
    weight_unit = models.CharField(max_length=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    sku = models.CharField(max_length=100, null=True, blank=True)
    value_amount = models.IntegerField(null=True, blank=True)
    value_currency = models.CharField(max_length=3, null=True, blank=True)   
    origin_country = models.CharField(max_length=3, null=True, blank=True)
    parent_id = models.CharField(max_length=255, null=True, blank=True)  #TODO: which parent_id
    metadata = models.ForeignKey(Items_metadata, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=100, null=True, blank=True)


class Parcel(models.Model):
    """
    model to create the PARCEL
    """
    parcel_id = models.CharField(max_length=255, null=True, blank=True)
    weight = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    packaging_type  = models.CharField(max_length=50, null=True, blank=True)
    package_preset = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)
    is_document = models.BooleanField(default=False)
    weight_unit = models.CharField(max_length=2, null=True, blank=True)
    dimension_unit = models.CharField(max_length=10)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=100, null=True, blank=True)
