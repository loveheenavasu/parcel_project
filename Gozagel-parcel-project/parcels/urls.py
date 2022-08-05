from django.urls import path
from parcels import views

urlpatterns = [
    path('parcels_post',views.parcels_post,name="parcels_post"),
]