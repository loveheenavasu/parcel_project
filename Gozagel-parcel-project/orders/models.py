
from importlib.metadata import requires
from shipments.models import Shipments
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import RESTRICT


# Create your models here.
class Orders(models.Model):
    shipment_id = models.ForeignKey(Shipments, on_delete=RESTRICT)
    user_id = models.OneToOneField(get_user_model(), on_delete=RESTRICT, blank=True)
    status = models.BooleanField(default=False, verbose_name="Payment Status")
    amount = models.IntegerField(verbose_name="Amount")
    stripe_payment_intent = models.CharField(
        max_length=200, verbose_name="Payment Intent"
    )


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=222,null=False,blank=False)
    last_name = models.CharField(max_length=222,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    Parcel_contents = models.CharField(max_length=250,null=False,blank=False)
    pracel_value = models.CharField(max_length=222,null=False,blank=False)
    sender_first_name = models.CharField(max_length=222,null=False,blank=False)
    sender_last_name = models.CharField(max_length=222,null=False,blank=False)
    sender_mail = models.EmailField(null=False,blank=False)
    sender_company = models.CharField(max_length=222,null=False,blank=False)
    sender_vat_number = models.CharField(max_length=222,null=False,blank=False)
    address = models.CharField(max_length=255,null=False,blank=False)
    sender_apartment = models.CharField(max_length=222,null=False,blank=False)
    city = models.CharField(max_length=255,null=False,blank=False)
    sender_county = models.CharField(max_length=222,null=False,blank=False)
    sender_province = models.CharField(max_length=222,null=False,blank=False)
    postal_code = models.CharField(max_length=222,null=False,blank=False)
    sender_Phone = models.CharField(max_length=222,null=False,blank=False)
    recipient_first_name = models.CharField(max_length=255,null=False,blank=False)
    recipient_last_name = models.CharField(max_length=255,null=False,blank=False)
    recipient_email = models.EmailField(null=False,blank=False)
    recipient_company = models.CharField(max_length=222,null=False,blank=False)
    recipient_vat_number = models.CharField(max_length=222,null=False,blank=False)
    recipient_address = models.CharField(max_length=255,null=False,blank=False)
    recipient_apartment = models.CharField(max_length=222,null=False,blank=False)
    recipient_city = models.CharField(max_length=255,null=False,blank=False)
    recipient_country = models.CharField(max_length=222,null=False,blank=False)
    recipient_province = models.CharField(max_length=222,null=False,blank=False)
    recipient_postal_code = models.CharField(max_length=222,null=False,blank=False)
    recipient_phone = models.CharField(max_length=222,null=False,blank=False)

   


class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
