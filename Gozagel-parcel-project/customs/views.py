from django.shortcuts import render

# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt

def custom_post(request):
    aa='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU5Njk1NDIxLCJpYXQiOjE2NTk2OTQ1MjEsImp0aSI6IjBhNDY4YzMzNjI5YzQzN2ZhYjE5M2U2YmYxOTc3ZTFhIiwidXNlcl9pZCI6Mn0.NZGJ5EAE0OWdo9MHxld2HoP9rtOxWniHFJJVhun--j0'
    hed = {'Authorization': 'Bearer ' + aa}
    api1 = "http://51.159.178.154:5002/v1/customs_info"
    data = {
        "commodities": [
            {
            "weight": 0,
            "weight_unit": "KG",
            "description": "string",
            "quantity": 1,
            "sku": "string",
            "value_amount": 0,
            "value_currency": "str",
            "origin_country": "str",
            
            "metadata": {}
            }
        ],
        "duty": {
            "paid_by": "sender",
            "currency": "EUR",
            "declared_value": 0,
            "account_number": "string",
            "bill_to": {
            "id": "string",
            "postal_code": "string",
            "city": "string",
            "federal_tax_id": "string",
            "state_tax_id": "string",
            "person_name": "string",
            "company_name": "string",
            "country_code": "AD",
            "email": "string",
            "phone_number": "123456789",
            "state_code": "string",
            "suburb": "string",
            "residential": False,
            "address_line1": "string",
            "address_line2": "string",
            "validate_location": False,
            "object_type": "address",
            "validation": {
                "success": True,
                "meta": {}
            }
            }
        },
        "content_type": "documents",
        "content_description": "string",
        "incoterm": "CFR",
        "invoice": "string",
        "invoice_date": "2022-07-11",
        "commercial_invoice": True,
        "certify": True,
        "signer": "string",
        "options": {}
        }
    req = requests.post(api1,json=data,headers=hed)
    data = req.json()
    print(data)
    
    