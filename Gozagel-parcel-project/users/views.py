# from django.shortcuts import render
import re
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect, render
from users.models import Contacts
from rest_framework.decorators import api_view
from .serializers import AddressSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    stu=Contacts.objects.all()
    serail=AddressSerializer(stu,many=True)
    return Response(serail.data)


@api_view(['POST'])
def create(request):
    data=request.data
    serial=AddressSerializer(data=data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data)
    else:
        return Response(serial.errors)


@api_view(['DELETE'])
def delete_address(request,id):
    try:
        student=Contacts.objects.get(id=id)
    except Contacts.DoesNotExist:
        return Response("id not found")
    if request.method=="DELETE":
        Contacts.objects.get(id=id).delete()
        return Response({"msg":"Data deleted"}) 

@api_view(['PUT'])
def update(request,id):
    try:
        student=Contacts.objects.get(id=id)
    except Contacts.DoesNotExist:
        return Response("id not found")
    if request.method=="PUT":
        data=request.data
        serial=AddressSerializer(student,data=data)
        if serial.is_valid():
            serial.save()
            return Response({"msg":"Data Updated"})
        else:
            return Response(serial.errors)










class DashboardView(TemplateView):
    template_name = "account/dashboard.html"


class ShipmentsView(TemplateView):
    template_name = "account/shipments.html"


def show_address(request):
    contact_list = Contacts.objects.all()
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'account/show_address.html', context)


class TicketsView(TemplateView):
    template_name = "account/tickets.html"


class DetailView(TemplateView):
    template_name = "account/detail.html"


def add_address(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        apartment_suit = request.POST['apartment_suit']
        city = request.POST['city']
        country = request.POST['country']
        province = request.POST['province']
        postal = request.POST['postal']
        obj=Contacts.objects.create(name=name,address=address,apartment_suit=apartment_suit,city=city,country=country,province=province,postal=postal)
        return redirect("show_address")
    return render(request, 'components/add_address.html')
  

    

# def Address(request):
#     contact_list = Contacts.objects.all()
#     print(contact_list)
#     context = {
#         "contact_list": contact_list,
#     }
#     return render(request, 'components/address_map.html', context)

