from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipmentsViewSet, ShipmentslabelViewSet
from shipments import views

router = DefaultRouter()


router.register(r'shipment', ShipmentsViewSet, basename='shipments'),
router.register(r'shipment_label', ShipmentslabelViewSet, basename='shipments_label'),

urlpatterns = [
     path('', include(router.urls)),
     path('shipment_post',views.shipment_post,name="shipment_post"),
     path('shipmentlabel_post',views.shipmentlabel_post,name="shipmentlabel_post"),

]