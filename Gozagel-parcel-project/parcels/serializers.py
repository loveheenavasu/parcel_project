# from curses import meta
# from dataclasses import field
# from django.urls import path, include
# from django.contrib.auth.models import User
from dataclasses import field
from rest_framework import serializers, viewsets
from .models import Parcel, Items


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class ParcelSerializer(serializers.ModelSerializer):
    # items = ItemsSerializer(read_only=True)

    class Meta:
        model = Parcel
        fields = '__all__'


# class parcel2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = parcel2
#         fields = '__all__'