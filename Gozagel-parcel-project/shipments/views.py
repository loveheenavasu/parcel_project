from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.views import generate_token, API_BASE_URL,SHIPMENT_ENDPOINT, USERNAME, PASSWORD, custom_response,SHIPMENTLABEL_ENDPOINT
from shipments.serializers import ShipmentSerializer,viewsets,ShipmentLabelSerializer
from shipments.models import Shipments
# Create your views here.


def shipment_post(request):    
    token = generate_token(USERNAME, PASSWORD)
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{SHIPMENT_ENDPOINT}"
    data= {
  "shipper": {
    "country_code": "EG",
    "city": "caior",
    "postal_code": "3753450",
    "validate_location": False,
    "shpment_reference": "hdsihsso",
    "validation": {
      "success": True,
      "meta": {}
    }
  },
  "recipient": {
    "country_code": "FR",
    "city": "caen",
    "postal_code": "14000",
    "validate_location": False,
    "validation": {
      "success": True,
      "meta": {}
    }
  },
  "parcels": [
    {
      "weight": 15,
      "width": 15,
      "height": 15,
      "length": 5,
      "is_document": False,
      "weight_unit": "KG",
      "dimension_unit": "CM",
      "items": [
        {
          "weight": 0,
          "weight_unit": "KG"
        }
      ],
      "object_type": "parcel"
    }
  ],
  "services": [],
  "options": {},
  "payment": {
    "paid_by": "sender"
  },
  "customs": {
    "incoterm": "CFR",
    "commodities": [
      {
        "weight": 0,
        "weight_unit": "KG"
      }
    ],
    "duty": {
      "paid_by": "sender",
      "currency": "EGP",
      "declared_value": 0,
      "bill_to": {
        "country_code": "AD",
        "phone_number": "98765432",
        "residential": False,
        "validate_location": False,
        "object_type": "address",
        "validation": {
          "success": True,
          "meta": {}
        }
      }
    },
    "object_type": "customs_info"
  },
  "carrier_name": "fedex",
  "carrier_id": "fedex_prod_test",
  "selected_rate": {
    "id": "car_bb8add0d0d53484eb75438e8b3347738",
    "object_type": "carrier",
    "carrier_name": "fedex",
    "carrier_id": "fedex_prod_test",
    "currency": "EGP",
    "test_mode": True
  },
  "meta": {},
  "selected_rate_id": "rat_fc8dc0ff4c784ce5973879e15de8247f",
  "test_mode": True
}
    req = requests.post(api,json=data,headers=hed)
    data = req.json()
    data['shipment_id'] = data.get('id')
    data['shipper_id'] = data.get('shipper.id')
    data['parcel_id'] = data.get('recipient.id')
    data['items_id'] = data.get('items.id')
    data['customs_id'] = data.get('customs.id')
    data['commodities_id'] = data.get('commodities.id')
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
            context = custom_response(status.HTTP_201_CREATED, data, "Created Successfully.")

            # if serializer.is_valid():
            #     self.perform_create(serializer)
            #     # user_obj = Address.objects.get(id=serializer.data["id"])
            #     # serializer = AddressSerializer(user_obj)
            #     context = custom_response(status.HTTP_201_CREATED, serializer.data, "Created Successfully.")
            # else:
            #     context = custom_response(status.HTTP_400_BAD_REQUEST, serializer.errors, "Unsuccessful.")
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



    
#*********************************************************SHIPMENT LABEL STARTS HERE******************************************************

def shipmentlabel_post(request):    
    token = generate_token(USERNAME, PASSWORD)
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{SHIPMENTLABEL_ENDPOINT}" 
    data= {     
  "selected_rate_id": "rat_2501e23953634f1bb9e0b223124827b3"
}
    req = requests.post(api,json=data,headers=hed)
    data = req.json()
    print(data)
    return data


class ShipmentslabelViewSet(viewsets.ModelViewSet):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentLabelSerializer
    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Shipments.objects.all()
            serializer = ShipmentLabelSerializer(queryset, many=True)
            context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))


    def create(self, request, *args, **kwargs): 
        # TODO: Make it unique
        data, context = [], {}
        try:
            data = shipmentlabel_post(request)
            serializer = ShipmentLabelSerializer(data=data)
            context = custom_response(status.HTTP_201_CREATED, data, "Created Successfully.")

            # if serializer.is_valid():
            #     self.perform_create(serializer)
            #     # user_obj = Address.objects.get(id=serializer.data["id"])
            #     # serializer = ShipmentLabelSerializer(user_obj)
            #     context = custom_response(status.HTTP_201_CREATED, serializer.data, "Created Successfully.")
            # else:
            #     context = custom_response(status.HTTP_400_BAD_REQUEST, serializer.errors, "Unsuccessful.")
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
                serializer = ShipmentLabelSerializer(user, data=request.data, partial=True)
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
                serializer = ShipmentLabelSerializer(get_user)
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