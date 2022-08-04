from django.urls import path
from django.urls import include
from .views import DashboardView, ShipmentsView, TicketsView, DetailView
from users import views
urlpatterns = [
    path("account/", include("allauth.urls")),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("shipments/", ShipmentsView.as_view(), name="shipments"),
    path("show_address/",views.show_address, name="show_address"),
    path("tickets/", TicketsView.as_view(), name="tickets"),
    path("detail/", DetailView.as_view(), name="detail"),
    path("add_address/",views.add_address,name="add_address"),
  
    path('index/',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('update/<int:id>',views.update,name="update"),
    path('delete_address/<int:id>',views.delete_address,name="delete_address"),
 
    # path('contact', views.contact, name='contacts'),
    # path('add_address', views.Address, name='contact')
]
