from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.views import generate_token, API_BASE_URL,SHIPMENT_ENDPOINT, USERNAME, PASSWORD, custom_response
from shipments.serializers import ShipmentSerializer,viewsets
from shipments.models import Shipments
# Create your views here.


def shipment_post(request):    
    token = generate_token(USERNAME, PASSWORD)
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{SHIPMENT_ENDPOINT}"
    data= {
            "shipper": {            
            "country_code": request.data.get('country_code'),
            "city": request.data.get('city'),
            "postal_code": request.data.get('postal_code'),
            "validate_location": request.data.get('validate_location'),
        },
        "recipient": {
            "country_code": request.data.get('country_code'),
            "city": request.data.get('city'),
            "postal_code": request.data.get('postal_code'),
            "validate_location": request.data.get('validate_location'),
        },
        "parcels": [
            {
            "weight": request.data.get('weight'),
            "width": request.data.get('width'),
            "height": request.data.get('height'),
            "length": request.data.get('length'),
            "is_document": request.data.get('is_document'),
            "weight_unit": request.data.get('weight_unit'),
            "dimension_unit": request.data.get('dimension_unit'),
            "items": [
                {
                "weight": request.data.get('weight'),
                "weight_unit": request.data.get('weight_unit'),
                }
            ],
            "object_type": request.data.get('object_type'),
            }
        ],
        "services": request.data.get('services'),
        "options": request.data.get('options'),
        "payment": {
            "paid_by": request.data.get('paid_by'),
        },
        "customs": {
            "incoterm": request.data.get('incoterm'),
            "commodities": [
            {
                "weight": request.data.get('weight'),
                "weight_unit": request.data.get('weight_unit'),
            }
            ],
            "duty": {
            "paid_by": request.data.get('paid_by'),
            "currency": request.data.get('currency'),
            "declared_value": request.data.get('declared_value'),
            "bill_to": {
                "country_code": request.data.get('country_code'),
                "phone_number": request.data.get('phone_number'),
                "residential": request.data.get('residential'),
                "validate_location": request.data.get('validate_location'),
                "object_type": request.data.get('object_type'),
            }
            },
            "object_type": request.data.get('object_type'),
        },
        "carrier_name": request.data.get('carrier_name'),
        "carrier_id": request.data.get('carrier_id'),
        "selected_rate": {
            "id": request.data.get('id'),
            "object_type": request.data.get('object_type'),
            "carrier_name": request.data.get('carrier_name'),
            "carrier_id": request.data.get('carrier_id'),
            "currency": request.data.get('currency'),
            "test_mode": request.data.get('test_mode'),
        },
        "meta": {},             
        "selected_rate_id": request.data.get('selected_rate_id'),
        "test_mode": request.data.get('test_mode'),
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