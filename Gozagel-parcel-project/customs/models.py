"""
Customs model
"""
# from multiprocessing import managers
# from pyexpat import model
# from statistics import mode
# from email.headerregistry import Address
from django.db import models
from address.models import Address

# Create your models here.

# class Customs_metadata(models.Model):
#     property_name  = models.CharField(max_length=250)

# class Validation(models.Model):
#     success = models.BooleanField(default=True)
#     meta_data = models.ForeignKey(Customs_metadata, on_delete=models.CASCADE)




PAID_BY = (
    ('SENDER', 'sender'),
    ('RECIPIENT','recipient'),
    ('THIRD_PARTY','third_party'),
)


class Commodities(models.Model):
    """
    Commodities model
    """
    commodities_id = models.CharField(max_length=255, null=True, blank=True)
    weight = models.IntegerField()
    weight_unit = models.CharField(max_length=2)
    description = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    sku = models.CharField(max_length=100, null=True, blank=True)
    value_amount = models.IntegerField(null=True, blank=True)
    value_currency = models.CharField(max_length=3, null=True, blank=True)
    origin_country = models.CharField(max_length=3, null=True, blank=True)
    parent_id = models.CharField(max_length=255)


# class Bill_to(models.Model):
#     """
#     Bill_to model
#     """
#     bill_to = models.ForeignKey(Address, on_delete=models.CASCADE)
#     object_type = models.CharField(max_length=255)
#     validation = models.ForeignKey(Validation, on_delete=CASCADE)
class Custom_Options(models.Model):

    aes = models.CharField(max_length=255)
    eel_pfc = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=255)
    nip_number = models.CharField(max_length=255)
    eori_number = models.CharField(max_length=255)
    vat_registration_number = models.CharField(max_length=255)

class Duty(models.Model):
    """
    Duty model
    """
    duty_id = models.CharField(max_length=255, null=True, blank=True)
    paid_by = models.CharField(max_length=50,choices=PAID_BY,default="sender") # TODO: make it option field
    currency = models.CharField(max_length=3, null=True, blank=True)
    declared_value = models.IntegerField(null=True, blank=True)
    account_number = models.CharField(max_length=250, null=True, blank=True)
    bill_to = models.ForeignKey(Address, on_delete=models.CASCADE)


class Custom(models.Model):
    """
    Custom model to store the customs data
    """
    Custom_id = models.CharField(max_length=255, null=True)
    commodities = models.ForeignKey(Commodities, on_delete=models.CASCADE)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=250, null=True, blank=True) #TODO: make it option field
    content_description = models.CharField(max_length=250, null=True, blank=True)
    incoterm = models.CharField(max_length=3, null=True, blank=True)
    invoice = models.CharField(max_length=50, null=True, blank=True)
    invoice_date = models.CharField(max_length=250, null=True, blank=True)
    commercial_invoice = models.BooleanField(null=True, blank=True)
    certify = models.BooleanField(null=True, blank=True)
    signer = models.CharField(max_length=50, null=True, blank=True)
    options = models.ForeignKey(Custom_Options, on_delete=models.CASCADE)
