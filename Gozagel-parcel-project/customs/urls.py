from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from customs import views

router = DefaultRouter()


router.register(r'customs', CustomViewSet, basename='custom'),

urlpatterns = [
     path('', include(router.urls)),
     path('custom_post',views.custom_post,name="custom_post"),

]