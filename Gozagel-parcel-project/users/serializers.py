from .models import Contacts
from django.forms import ValidationError
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"
