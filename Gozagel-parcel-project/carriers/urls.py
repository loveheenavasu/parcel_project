from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from carriers.views import *
from carriers import views

router = DefaultRouter()


router.register(r'carrier', CarrierViewSet, basename='carrier'),

urlpatterns = [
     path('carrier_get',views.carrier_get ,name="carrier_get"),
     path('', include(router.urls)),
]


