import imp
from unicodedata import name
from django.urls import path
from orders.views import *
urlpatterns = [
    path("book/", BookView.as_view(), name ='book'),
    path("book/checkout/", CheckoutView.as_view(), name="checkout"),
    path("book/success/", SuccessView.as_view(), name="success"),
    path("book/cancel/", CancelView.as_view(), name="cancel"),
    path("book/webhook/", WebhookView.as_view(), name="webhook"),

    # Api File Url
    path("api", api, name="api"),
    path("trackingPage", trackingPage, name="trackingPage"),
    path("tracking_data", tracking_data, name="tracking_data"),


]

