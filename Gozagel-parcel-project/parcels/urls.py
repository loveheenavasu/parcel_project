from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from parcels.views import *
from parcels import views

router = DefaultRouter()


router.register(r'parcels', ParcelViewSet, basename='Parcel'),

urlpatterns = [
     path('parcel_post',views.parcel_post ,name="parcel_post"),
     path('', include(router.urls)),
]