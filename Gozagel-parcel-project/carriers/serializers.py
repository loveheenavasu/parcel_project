from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from carriers.models import Carriers


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriers
        fields = '__all__'



