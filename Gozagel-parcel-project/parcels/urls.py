from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import *
from . import views

router = DefaultRouter()


router.register(r'parcels', ParcelViewSet, basename='Parcel'),
router.register(r'items',ItemViewSet, basename= 'items')

urlpatterns = [
     path('', include(router.urls)),
     path('parcel_post', views.parcel_post, name="parcel_post"), 
     path('item_post', views.parcel_post, name="item_post"),
]