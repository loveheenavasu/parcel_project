from importlib.metadata import metadata
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.views import generate_token, API_BASE_URL, PARCEL_ENDPOINT, USERNAME, PASSWORD, custom_response
from .serializers import *
from .models import Items_metadata, Parcel, Items


def parcel_post(request):
    token = generate_token(USERNAME, PASSWORD)
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{PARCEL_ENDPOINT}"
    data = {
    "weight": 1,
    "width": 1,
    "height": 1,
    "length": 1,
    "packaging_type": "small_box",
    "package_preset": "something",
    "description": "birth card",
    "content": "card",
    "is_document": True,
    "weight_unit": "KG",
    "dimension_unit": "CM",
    "items": [
        {
            "weight": 1,
            "weight_unit": "KG",
            "description": "nothing to write right now",
            "quantity": 1,
            "sku": "string",
            "value_amount": 0,
            "value_currency": "INR",
            "origin_country": "IND",
            "metadata": {}
        }
    ],
    "reference_number": "123456789"
}   
    
    req = requests.post(api,json=data,headers=hed)
    data = req.json()
    data['parcel_id'] = data.get('id')
    print(data)
    return data
    

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Parcel.objects.all()
            serializer = ParcelSerializer(queryset, many=True)
            context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))


    def create(self, request, *args, **kwargs): 
        # TODO: Make it unique
        data, context = [], {}
        try:
            data = parcel_post(request)
            serializer = ParcelSerializer(data=data)
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














































































































































class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Parcel.objects.all()
            serializer = ParcelSerializer(queryset, many=True)
            # context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

        

    def create(self, request, *args, **kwargs): 
        # TODO: Make it unique
        data, context = [], {}
        try:
            data = parcel_post(request)
            serializer = ParcelSerializer(data=data)

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





def item_post(request):
    token = generate_token("dev@example.com", "testdevex")
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{PARCEL_ENDPOINT}"
    data = {
        "weight": request.data.get('weight'),
        "weight_unit": request.data.get('weight_unit'),
        "description": request.data.get('description'),
        "quantity": request.data.get('quantity'),
        "sku": request.data.get('sku'),
        "value_amount": request.data.get('value_currency'),
        "origin_country": request.data.get('origin_country'),
        "parent_id  ": request.data.get('parent_id'),
        "object_type": request.data.get('object_type'),
        "metadata": request.data.get('metadata')
        
    }
    
    req = requests.post(api,json=data,headers=hed)
    data = req.json()
    data['items_id'] = data.get('id')
    print(data)
    return data


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Items.objects.all()
            serializer = ItemsSerializer(queryset, many=True)
            context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

        

    def create(self, request, *args, **kwargs): 
        # TODO: Make it unique
        data, context = [], {}
        try:
            data = parcel_post(request)
            serializer = ItemsSerializer(data=data)

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


# def parcel_post(request):
#     token = generate_token(USERNAME, PASSWORD)
#     header = {"Authorization": f"Bearer {token.get('access')}"}
#     api = f"{API_BASE_URL}{PARCEL_ENDPOINT}"
#     data = {
#         "weight": request.data.get('weight'),
#         "width": request.data.get('width'),
#         "height": request.data.get('height'),
#         "length": request.data.get('length'),
#         "packaging_type": request.data.get('packaging_type'),
#         "package_preset": request.data.get('package_preset'),
#         "description": request.data.get('description'),
#         "content": request.data.get('content'),
#         "quantity": request.data.get('quantity'),
#         "is_document": request.data.get('is_document'),
#         "weight_unit": request.data.get('weight_unit'),
#         "dimension_unit": request.data.get('dimension_unit'),
#         "reference_number": request.data.get('reference_number')
#     }
#     req = requests.post(api, json=data, headers=header)
#     data = req.json()
#     data['parcel_id'] = data.get('id')
#     return data


# class ParcelViewSet(ModelViewSet):
#     queryset = Parcel.objects.all()
#     serializer_class = ParcelSerializer

#     def list(self, request, *args, **kwargs):
#         data, context = [], {}
#         try:
#             queryset = Parcel.objects.all()
#             serializer = ParcelSerializer(queryset, many=True)
#             context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
#         except Exception as error:
#             context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
#         return JsonResponse(context, safe=False, status=context.get("status"))


#     def create(self, request, *args, **kwargs):
#         # TODO: Make it unique
#         data, context = [], {}
#         try:
#             data = parcel_post(request)
#             serializer = ParcelSerializer(data=data)
    
#             if serializer.is_valid():
#                 self.perform_create(serializer)
#                 # user_obj = Address.objects.get(id=serializer.data["id"])
#                 # serializer = AddressSerializer(user_obj)
#                 context = custom_response(status.HTTP_201_CREATED, serializer.data, "Created Successfully.")
#             else:
#                 context = custom_response(status.HTTP_400_BAD_REQUEST, serializer.errors, "Unsuccessful.")
#         except Exception as error:
#             context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
#         return JsonResponse(context, safe=False)


#     def create(self, request, *args, **kwargs):
#         # TODO: Make it unique
#         data, context = [], {}
#         try:
#             parcel_data = parcel_post(request)
#             parcel_items_data = parcel_data.pop('items')[0]
#             parcel_items_data['parcel_items_id'] = parcel_items_data.pop('id')
#             # parcel_items_metadata = parcel_items_data.pop('metadata')
#             print("parcel_items_data", parcel_items_data)
#             item_serial = ItemsSerializer(data=parcel_items_data)


#             '''meta_data'''
#             Items_metadata_data = parcel_items_data.pop('metadata')
#             Items_metadata_data['id'] = Items_metadata_data
#             meta_serial = metaSerializer(data=Items_metadata_data)
#             if item_serial.is_valid() and meta_serial.is_valid():
#                 item_serial.save() 
#                 meta_serial.save()
                
#                 self.perform_create(item_serial)

#             parcel_data['items'] = item_serial.data.get('id')
#             serializer = ParcelSerializer(data=parcel_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 context = custom_response(status.HTTP_201_CREATED, serializer.data, "Created Successfully.")
#             else:
#                 context = custom_response(status.HTTP_400_BAD_REQUEST, serializer.errors, "Unsuccessful.")
#         except Exception as error:
#             context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
#         return JsonResponse(context, safe=False)

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

    # def partial_update(self, request, pk):
    #     data = []
    #     try:
    #         try:
    #             queryset = Parcel.objects.all()
    #             user = get_object_or_404(queryset, pk=pk)
    #             serializer = ParcelSerializer(user, data=request.data, partial=True)
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 user_obj = Parcel.objects.get(id=serializer.data["id"])
    #                 serializer = Parcel(user_obj)
    #                 context = custom_response(status.HTTP_200_OK, serializer.data, "Updated Successfully.")
    #             else:
    #                 context = custom_response(status.HTTP_202_ACCEPTED, serializer.errors, "Unsuccessful.")
    #         except Exception as error:
    #             context = custom_response(status.HTTP_404_NOT_FOUND)
    #     except Exception as error:
    #         context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
    #     return Response(context, status=context.get("status"))

    # def retrieve(self, request, pk=None):
    #     data = []
    #     context = {}
    #     try:
    #         try:
    #             get_user = Parcel.objects.get(id=pk)
    #             serializer = ParcelSerializer(get_user)
    #             context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
    #         except Exception as error:
    #             context = custom_response(status.HTTP_404_NOT_FOUND)
    #     except Exception as error:
    #         context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
    #     return JsonResponse(context, status=context.get("status"), safe=False)

    # def destroy(self, request, *args, **kwargs):
    #     data, context = [], {}
    #     try:
    #         try:
    #             user = self.get_object()
    #             user.delete()
    #             context = custom_response(status.HTTP_200_OK, message="Deleted Successfully")
    #         except Exception as error:
    #             context = custom_response(status.HTTP_404_NOT_FOUND)
    #     except Exception as error:
    #         context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
    #     return JsonResponse(context, status=context.get('status'), safe=False)
