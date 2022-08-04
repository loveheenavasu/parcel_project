import imp
from django.urls import path
from .views import QuoteView, QuoteLogInView

urlpatterns = [
    path("quote/", QuoteView.as_view(), name="quote"),
]
