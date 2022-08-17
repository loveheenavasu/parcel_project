import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.views import generate_token, API_BASE_URL, ADDRESS_ENDPOINT, USERNAME, PASSWORD, custom_response
from .serializers import *
1

def address_post(request):
    token = generate_token("dev@example.com", "testdevex")
    hed = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{ADDRESS_ENDPOINT}"
    data= {
    "postal_code": "tr567",
    "city": "palampur",
    "federal_tax_id": "34567890",
    "state_tax_id": "3456789",
    "person_name": "oiuytfghj",
    "company_name": "xyz",
    "country_code": "EG",
    "email": "xctfyvgb98765enjrewohbvg@gmail.com",
    "phone_number": "798765432",
    "state_code": "987vbn",
    "suburb": None,
    "residential": False,
    "address_line1": "abc",
    "address_line2": "abc",
    "validate_location": False
}
    
    req = requests.post(api,json=data,headers=hed)
    data = req.json()
    data['address_id'] = data.get('id')
    print(data)
    return data


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def list(self, request, *args, **kwargs):
        data, context = [], {}
        try:
            queryset = Address.objects.all()
            serializer = AddressSerializer(queryset, many=True)
            context = custom_response(status.HTTP_200_OK, serializer.data, "Fetched Successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))

        

    def create(self, request, *args, **kwargs): 
        # TODO: Make it unique
        data, context = [], {}
        try:
            data = address_post(request)
            serializer = AddressSerializer(data=data)

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
                queryset = Address.objects.all()
                user = get_object_or_404(queryset, pk=pk)
                serializer = AddressSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    user_obj = Address.objects.get(id=serializer.data["id"])
                    serializer = Address(user_obj)
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
                serializer = AddressSerializer(get_user)
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






                

