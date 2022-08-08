from urllib import request
from django.views.generic import TemplateView    


import requests


API_BASE_URL = 'http://51.159.178.154:5002' 
ADDRESS_ENDPOINT = "/v1/addresses"

USERNAME = 'dev@example.com'
PASSWORD = 'testdevex'



def generate_token(email, password): 
    """generate token to access the API's""" 
    endpoint='/api/token'
    api = f"{API_BASE_URL}{endpoint}"
    data= {
        "email": email,
        "password": password
        }   
    req=requests.post(api,json=data)
    token=req.json()
    return token

generate_token("dev@example.com", "testdevex")


class HomeView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"


class FaqView(TemplateView):
    template_name = "faq.html"

