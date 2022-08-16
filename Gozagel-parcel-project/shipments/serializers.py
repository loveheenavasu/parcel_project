from pyexpat import model
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from shipments.models import Shipments


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = '__all__'

class ShipmentLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = '__all__'
        

