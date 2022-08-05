from django.urls import path
from customs import views

urlpatterns = [
    path('custom_post',views.custom_post,name="custom_post"),
]