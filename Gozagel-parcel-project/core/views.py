import requests
from django.views.generic import TemplateView    


USERNAME = 'dev@example.com'
PASSWORD = 'testdevex'
API_BASE_URL = 'http://51.159.178.154:5002' 
ADDRESS_ENDPOINT = "/v1/addresses"
PARCEL_ENDPOINT = '/v1/parcels'


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

# generate_token("dev@example.com", "testdevex")


def custom_response(status, data=[], message=""):
    """return custom response for all the APIs"""
    if status == 404:
        if not message:
            message = "Data not found."
        context = {
            "status": status,
            "message": message,
            "data": data
        }
    elif status == 400 or status == 202:
        error_list = list()
        if isinstance(data, str):
            message = data
            context = {
                "status": status,
                "message": message,
                "data": []
            }
        else:
            for i, j in data.items():
                j = "".join(j)
                message = f"{i}: {j}"
                error_list.append(message)

            context = {
                "status": status,
                "message": ", ".join(error_list),
                "data": []
            }
    elif status == 409:
        context = {
            "status": status,
            "message": "Already exists",
            "data": []
        }
    else:
        context = {
            "status": status,
            "message": message,
            "data": data
        }
    return context

class HomeView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"


class FaqView(TemplateView):
    template_name = "faq.html"

