from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from address import views

router = DefaultRouter()


router.register(r'address', AddressViewSet, basename='address'),

urlpatterns = [
     path('', include(router.urls)),
     path('address_post',views.address_post,name="address_post"),

]