from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.views import generate_token, API_BASE_URL,ADDRESS_ENDPOINT, USERNAME, PASSWORD
from shipments.serializers import *

# Create your views here.
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

def shipment_post(request):
    token = generate_token("dev@example.com", "testdevex")
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{ADDRESS_ENDPOINT}"
    data= {
  "shipper": {
    "postal_code": "string",
    "city": "string",
    "federal_tax_id": "string",
    "state_tax_id": "string",
    "person_name": "string",
    "company_name": "string",
    "country_code": "AD",
    "email": "string",
    "phone_number": "string",
    "state_code": "string",
    "suburb": "string",
    "residential": False,
    "address_line1": "string",
    "address_line2": "string",
    "validate_location": False
  },
  "recipient": {
    "postal_code": "string",
    "city": "string",
    "federal_tax_id": "string",
    "state_tax_id": "string",
    "person_name": "string",
    "company_name": "string",
    "country_code": "AD",
    "email": "string",
    "phone_number": "string",
    "state_code": "string",
    "suburb": "string",
    "residential": False,
    "address_line1": "string",
    "address_line2": "string",
    "validate_location": False
  },
  "parcels": [
    {
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
  ],
  "options": {},
  "payment": {
    "paid_by": "sender"
  },
  "customs": {
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
        "parent_id": "string",
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
        "phone_number": "string",
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
    "invoice_date": "string",
    "commercial_invoice": True,
    "certify": True,
    "signer": "string",
    "options": {}
  },
  "reference": "string",
  "label_type": "PDF",
  "service": "string",
  "services": [],
  "carrier_ids": [],
  "metadata": {}
}
    
    req = requests.post(api,json=data,headers=hed)
    data = req.json()
    data['address_id'] = data.get('id')
    print(data)
    return data


class ShipmentsViewSet(viewsets.ModelViewSet):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Shipments.objects.all()
            serializer = ShipmentSerializer(queryset, many=True)
            context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

    def create(self, request, *args, **kwargs): 
        # TODO: Make it unique
        data, context = [], {}
        try:
            data = shipment_post(request)
            serializer = ShipmentSerializer(data=data)

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
                queryset = Shipments.objects.all()
                user = get_object_or_404(queryset, pk=pk)
                serializer = ShipmentSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    user_obj = Shipments.objects.get(id=serializer.data["id"])
                    serializer = Shipments(user_obj)
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
                get_user = Shipments.objects.get(id=pk)
                serializer = ShipmentSerializer(get_user)
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