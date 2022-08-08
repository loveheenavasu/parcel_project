# from curses import meta
# from dataclasses import field
# from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from parcels.models import Parcel, Items

class ItemsSerializer(serializers.Serializer):
    class Meta:
        model = Items
        fields = '__all__'


class ParcelSerializer(serializers.ModelSerializer):
    items = ItemsSerializer 
    class Meta:
        model = Parcel
        fields = '__all__'