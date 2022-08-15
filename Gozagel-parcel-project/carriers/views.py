import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.views import generate_token, API_BASE_URL,ADDRESS_ENDPOINT, USERNAME, PASSWORD
from carriers.serializers import *


def custom_response(status, data=[], message=""):
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

def carrier_get(request):
    token = generate_token("dev@example.com", "testdevex")
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{ADDRESS_ENDPOINT}"
    data= {
        "postal_code": request.data.get('postal_code'),
        "city": request.data.get('city'),
        "federal_tax_id": request.data.get('federal_tax_id'),
        "state_tax_id": request.data.get('state_tax_id'),
        "person_name": request.data.get('person_name'),
        "company_name": request.data.get('company_name'),
        "country_code": request.data.get('country_code'),
        "email": request.data.get('email'),
        "phone_number": request.data.get('phone_number'),
        "state_code": request.data.get('state_code'),
        "suburb": request.data.get('suburb'),
        "residential": request.data.get('residential'),
        "address_line1": request.data.get('address_line1'),
        "address_line2": request.data.get('address_line2'),
        "validate_location":request.data.get('validate_location'),
    }
    
    req = requests.get(api,headers=hed)
    data = req.json()
    data['address_id'] = data.get('id')
    print(data)
    return data
   
class CarrierViewSet(viewsets.ModelViewSet):
    queryset = Carriers.objects.all()
    serializer_class = CarrierSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            # data = carrier_get()
            queryset = Carriers.objects.all()
            serializer = CarrierSerializer(queryset, many=True)
            context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))
