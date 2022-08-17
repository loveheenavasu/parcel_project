from django.shortcuts import render

# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.views import generate_token, API_BASE_URL,ADDRESS_ENDPOINT, USERNAME, PASSWORD,custom_response
from customs.serializers import *



def custom_post(request):
    token = generate_token(USERNAME, PASSWORD)
    hed = {"Authorization": f"Bearer {token.get('access')}"}
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


class CustomViewSet(viewsets.ModelViewSet):
       queryset = Custom.objects.all()
       serializer_class = CustomSerializer

def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Custom.objects.all()
            serializer = CustomSerializer(queryset, many=True)
            context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))
def create(self, request, *args, **kwargs): 
        # TODO: Make it unique
        data, context = [], {}
        try:
            data = custom_post(request)
            serializer = CustomSerializer(data=data)

            if serializer.is_valid():
                self.perform_create(serializer)
                # user_obj = Address.objects.get(id=serializer.data["id"])
                # serializer = AddressSerializer(user_obj)
                context = custom_response(status.HTTP_201_CREATED, serializer.data, "Created Successfully.")
            else:
                context = custom_response(status.HTTP_400_BAD_REQUEST, serializer.errors, "Unsuccessful.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)

    #     custom_data = {
    #         "status": "success",
    #         "message": "Created Successfully",
    #         "data": serializer.data
    #     }

    #     return Response(custom_data, status=status.HTTP_201_CREATED)
def partial_update(self, request, pk):
        data = []
        try:
            try:
                queryset = Custom.objects.all()
                user = get_object_or_404(queryset, pk=pk)
                serializer = CustomSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    user_obj = Custom.objects.get(id=serializer.data["id"])
                    serializer = Custom(user_obj)
                    context = custom_response(status.HTTP_200_OK, serializer.data, "Updated Successfully.")
                else:
                    context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, "Unsuccessful.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return Response(context, status=context.get("status"))

def retrieve(self, request, pk=None):
        data = []
        context = {}
        try:
            try:
                get_user = Address.objects.get(id=pk)
                serializer = CustomSerializer(get_user)
                context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get("status"), safe=False)

def destroy(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            try:
                user = self.get_object()
                user.delete()
                context = custom_response(status.HTTP_200_OK, message="Deleted Successfully")
            except Exception as error:
                context = custom_response(status.HTTP_404_NOT_FOUND)
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, status=context.get('status'), safe=False)

    
    