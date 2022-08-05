from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt




def parcels_post(request):
    aa='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU5Njk0NjMwLCJpYXQiOjE2NTk2OTM3MzAsImp0aSI6ImNlYjQ3YTc3MWIzZjRiMTk4YTM1YWQxZTU4ODEzYzUzIiwidXNlcl9pZCI6Mn0.vHJs0ZvCYc7rpPGrRuuKuzN4NEiAcbsli0oWzAXGz_4'
    hed = {'Authorization': 'Bearer ' + aa}
    api1 = "http://51.159.178.154:5002/v1/parcels"
    data = {
  "weight": 0,
  "width": 0,
  "height": 0,
  "length": 0,
  "packaging_type": "string",
  "package_preset": "string",
  "description": "string",
  "content": "string",
  "is_document": False,
  "weight_unit": "KG",
  "dimension_unit": "CM",
  "items": [
    {
      "weight": 0,
      "weight_unit": "KG",
      "description": "string",
      "quantity": 1,
      "sku": "string",
      "value_amount": 0,
      "value_currency": "str",
      "origin_country": "str",
      "parent_id": "string",
      "metadata": {}
    }
  ],
  "reference_number": "string"
}
    req = requests.post(api1,json=data,headers=hed)
    data = req.json()
    print(data)