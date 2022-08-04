from django.urls import path
from core import views
from .views import HomeView, ContactView, AboutView, FaqView

urlpatterns = [
    path("home/", HomeView.as_view(), name="HomeViews"),
    path("", HomeView.as_view(), name="HomeView"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("faq/", FaqView.as_view(), name="faq"),

]
