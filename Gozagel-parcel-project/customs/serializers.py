from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from customs.models import *


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = '__all__'