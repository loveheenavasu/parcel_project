from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from shipments import views

router = DefaultRouter()


router.register(r'shipment', ShipmentsViewSet, basename='shipments'),

urlpatterns = [
     path('', include(router.urls)),
      path('shipment_post',views.shipment_post,name="shipment_post"),

]