import os
import re
import sqlite3
import requests
from users.models import Contacts
from django.core import serializers

import folium
import geocoder
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, TemplateView, View
import stripe
import json
from .models import Search
from .forms import SearchForm
from orders.models import Customer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

stripe.api_key = "sk_test_51IdCfjHw4HZ2kCHRfhsYcX1NvBXuPGWbRoByMri1jXBtN9whbndpxz2yN0IuDhhZE1xqqwp8yQ3P7YPn7HD5tnLa007K98cNaM"


class BookView(View):
    def get(self, request):
        """As we provide with the order form, we calculate prices for insured and uninsured packages with and without
        taxes """
        rates = request.session["rates"]
        rate_id = request.GET["rate"]
        for rate in rates:
            if rate_id in rate["id"]:
                final_rate = rate
                break
            else:
                pass
        insurance = format(float(final_rate["rate"]) * 0.1, ".2f")
        final_insured = format(
            ((float(final_rate["rate"]) * 1.14) + (float(insurance) * 1.14)),
            ".2f",
        )
        final_not_insured = format((float(final_rate["rate"]) * 1.14), ".2f")
        taxes_insured = format(
            (float(insurance) * 0.1 + float(final_rate["rate"]) * 0.14), ".2f"
        )
        taxes_not_insured = format((float(final_rate["rate"]) * 0.14), ".2f")
        request.session["final_not_insured"] = final_not_insured
        request.session["final_rate"] = final_rate
        request.session.modified = True
        # Data get in Contects model define in users app
        obj_datas = Contacts.objects.all()
        obj_data =(list(obj_datas.values()))
        return render(
            request,
            context={
                "final_rate": final_rate,
                "insurance": insurance,
                "final_insured": final_insured,
                "final_not_insured": final_not_insured,
                "taxes_insured": taxes_insured,
                "taxes_not_insured": taxes_not_insured,
                'obj_data': obj_data,
            },
            template_name="orders/book.html",
        )


class CheckoutView(TemplateView):
    def get(self, request):
        return render(request, 'orders/book.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('Firstname')
        last_name = postData.get('last')
        email = postData.get('email')
        Parcel_contents = postData.get('parcel')
        pracel_value = postData.get('value')
        sender_first_name = postData.get('sender-first-name')
        sender_last_name = postData.get('sender-last-name')
        sender_mail = postData.get('sender-email')
        sender_company = postData.get('sender-company')
        sender_vat_number = postData.get('sender-tax')
        address = postData.get('sender-address')
        sender_apartment = postData.get('sender-apartment')
        city = postData.get('sender-city')
        sender_county = postData.get('sender-country')
        sender_province = postData.get('sender-province')
        postal_code = postData.get('sender-postal-code')
        sender_Phone = postData.get('sender-phone')
        recipient_first_name = postData.get('recipient-first-name')
        recipient_last_name = postData.get('recipient-last-name')
        recipient_email = postData.get('recipient-email')
        recipient_company = postData.get('recipient-company')
        recipient_vat_number = postData.get('recipient-tax')
        recipient_address = postData.get('recipient-address')
        recipient_apartment = postData.get('recipient-apartment')
        recipient_city = postData.get('recipient-city')
        recipient_country = postData.get('recipient-countrye')
        recipient_province = postData.get('recipient-province')
        recipient_postal_code = postData.get('recipient-postal-code')
        recipient_phone = postData.get('recipient-phone')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'Parcel_contents': Parcel_contents,
            'pracel_value': pracel_value,
            'sender_first_name': sender_first_name,
            'sender_last_name': sender_last_name,
            'sender_mail': sender_mail,
            'sender_company': sender_company,
            'sender_vat_number': sender_vat_number,
            'address': address,
            'sender_apartment': sender_apartment,
            'city': city,
            'sender_county': sender_county,
            'sender_province': sender_province,
            'postal_code': postal_code,
            'sender_Phone': sender_Phone,
            'recipient_first_name': recipient_first_name,
            'recipient_last_name': recipient_last_name,
            'recipient_email': recipient_email,
            'recipient_company': recipient_company,
            'recipient_vat_number': recipient_vat_number,
            'recipient_address': recipient_address,
            'recipient_apartment': recipient_apartment,
            'recipient_city': recipient_city,
            'recipient_country': recipient_country,
            'recipient_province': recipient_province,
            'recipient_postal_code': recipient_postal_code,
            'recipient_phone': recipient_phone,
        }
        customer = Customer(first_name=first_name, last_name=last_name, email=email, Parcel_contents=Parcel_contents,
                            pracel_value=pracel_value
                            , sender_first_name=sender_first_name, sender_last_name=sender_last_name,
                            sender_mail=sender_mail, sender_company=sender_company, sender_vat_number=sender_vat_number,
                            address=address,
                            sender_apartment=sender_apartment,
                            city=city, sender_county=sender_county, sender_province=sender_province,
                            postal_code=postal_code,
                            sender_Phone=sender_Phone,
                            recipient_first_name=recipient_first_name, recipient_last_name=recipient_last_name,
                            recipient_email=recipient_email, recipient_company=recipient_company,
                            recipient_vat_number=recipient_vat_number,
                            recipient_address=recipient_address, recipient_apartment=recipient_apartment,
                            recipient_city=recipient_city, recipient_country=recipient_country,
                            recipient_province=recipient_province,
                            recipient_postal_code=recipient_postal_code, recipient_phone=recipient_phone
                            )
        customer.save()
        error_message = self.validateCustomer(customer)
        if not error_message:
            """post request to stripe to validate order"""
            total = float(request.session["final_not_insured"])
            total_cents = int(total * 100)
            name = f"Parcel from {request.session['parcel']['from']} {request.session['parcel']['to']}"
            try:
                checkout_session = stripe.checkout.Session.create(
                    customer_email=email,
                    submit_type="pay",
                    line_items=[
                        {
                            "price_data": {
                                "currency": "EUR",
                                "product_data": {"name": name},
                                "unit_amount": total_cents,
                                "tax_behavior": "inclusive",
                            },
                            "quantity": 1,
                        },
                    ],
                    payment_intent_data={"metadata": {"hello": "fren"}},
                    payment_method_types=[
                        "card",
                    ],
                    mode="payment",
                    success_url="http://127.0.0.1:8000/book" + "/success",
                    cancel_url="http://127.0.0.1:8000/book" + "/cancel",
                )
            except Exception as e:
                return str(e)
            return redirect(checkout_session.url, code=303)
        else:
            data = {
                'error': error_message,
                'values': value
            }
            print(data)
            return render(request, 'orders/book.html', data)

    def validateCustomer(self, customer):
        error_message = {}
        if not customer.first_name:
            error_message['first_name'] = "First Name Required !!"
        elif len(customer.first_name) < 2:
            error_message['first_name'] = 'First Name must be 2 char long or more'
        elif len(customer.first_name) > 50:
            error_message['first_name'] = 'First Name Minimum 50 Char'
        if not customer.last_name:
            error_message['last_name'] = 'Last Name Required'
        elif len(customer.last_name) < 2:
            error_message['last_name'] = 'Last Name must be 2 char long or more'
        elif len(customer.last_name) > 50:
            error_message['last_name'] = 'Last Name Minimum 50 Char'
        if not customer.email:
            error_message['email'] = 'Email is required and should be valid with @domain'
        elif len(customer.email) < 4:
            error_message['email'] = 'Email  must be 4 char long or more'
        elif len(customer.email) > 255:
            error_message['email'] = 'Email Name Minimum 255 Char'
        if not customer.Parcel_contents:
            error_message['Parcel_contents'] = ' Parcel contents Required'
      
        elif len(customer.Parcel_contents) > 200:
            error_message['Parcel_contents'] = 'Parcel Content  Minimum 200 Char'
        if not customer.pracel_value:
            error_message['pracel_value'] = ' Parcel Value Required'
        
        elif len(customer.pracel_value) > 8:
            error_message['pracel_value'] = 'Parcel Value  Minimum 8 Char'

        # Sender form information
        if not customer.sender_first_name:
            error_message['sender_first_name'] = "Sender First Name Required !!"
        elif len(customer.sender_first_name) < 2:
            error_message['sender_first_name'] = 'Sender first  must be 2 char long or more'
        elif len(customer.sender_first_name) > 50:
            error_message['sender_first_name'] = 'Sender first  Name Minimum 50 Char'
        if not customer.sender_last_name:
            error_message['sender_last_name'] = 'Sender Last Name Required'
        elif len(customer.sender_last_name) < 2:
            error_message['sender_last_name'] = 'Sender Last name  must be 2 char long or more'
        elif len(customer.sender_last_name) > 50:
            error_message['sender_last_name'] = 'Sender Last  Name Minimum 50 Char'

        if len(customer.sender_mail) > 0:
            if len(customer.sender_mail) > 255:
                error_message['sender_mail'] = 'Sender Company must be Minimum 225 Char'
            elif len(customer.sender_mail) < 4:
                error_message['sender_mail'] = 'Sender Company must be 4 char long'

        if len(customer.sender_company) > 0:
            if len(customer.sender_company) > 50:
                error_message['sender_company'] = 'Sender Company must be Minimum 50 Char'
            elif len(customer.sender_company) < 2:
                error_message['sender_company'] = 'Sender Company must be 2 char long'

        if len(customer.sender_vat_number) > 0:
            if len(customer.sender_vat_number) > 25:
                error_message['sender_vat_number'] = 'Sender vat number must be Minimum 25 Char'
          
        if not customer.address:
            error_message['address'] = 'Sender address is Required'
        elif len(customer.address) < 2:
            error_message['address'] = 'Sender address name  must be 2 char long or more'
        elif len(customer.address) > 90:
            error_message['address'] = 'Sender Address  Name Minimum 90 Char'

        if len(customer.sender_apartment) > 0:
            if len(customer.sender_apartment) > 20:
                error_message['sender_apartment'] = 'Sender apartment suit must be Minimum 20 Char'
          
        if not customer.city:
            error_message['city'] = 'Sender city is Required'
       
        elif len(customer.city) > 45:
            error_message['city'] = 'Sender City   Minimum 45 Char'

        if not customer.sender_county:
            error_message['sender_county'] = "Sender Country Name Required !!"
        elif len(customer.sender_county) < 2:
            error_message['sender_county'] = 'Sender Country  must be 2 char long or more'
        elif len(customer.sender_county) > 56:
            error_message['sender_county'] = 'Sender Country  Name Minimum 56 Char'

        if len(customer.sender_province) > 0:
            if len(customer.sender_province) > 56:
                error_message['sender_province'] = 'Sender province must be Minimum 56 Char'
           

        if not customer.postal_code:
            error_message['postal_code'] = 'Sender postal code is Required'
      
        elif len(customer.postal_code) > 12:
            error_message['postal_code'] = 'Postal Code   Minimum 12 Char'

        if len(customer.sender_Phone) > 0:
            if len(customer.sender_Phone) > 15:
                error_message['sender_Phone'] = 'Sender phone number must be Minimum 15 Char'
            
        # Recipient Form information
        if not customer.recipient_first_name:
            error_message['recipient_first_name'] = "Recipient First Name Required !!"
        elif len(customer.recipient_first_name) < 2:
            error_message['recipient_first_name'] = 'Recipient First name  must be 2 char long or more'
        elif len(customer.recipient_first_name) > 50:
            error_message['recipient_first_name'] = 'Recipient First name   Minimum 50 Char'

        if not customer.recipient_last_name:
            error_message['recipient_last_name'] = 'Recipient Last Name Required'
        elif len(customer.recipient_last_name) < 2:
            error_message['recipient_last_name'] = 'Recipient Last name  must be 2 char long or more'
        elif len(customer.recipient_last_name) > 50:
            error_message['recipient_last_name'] = 'Recipient Last name   Minimum 50 Char'

        if len(customer.recipient_email) > 0:
            if len(customer.recipient_email) > 225:
                error_message['recipient_email'] = 'Recipient Email must be Minimum 225 Char'
            elif len(customer.recipient_email) < 4:
                error_message['recipient_email'] = 'Recipient Email must be 4 char long'

        if len(customer.recipient_company) > 0:
            if len(customer.recipient_company) > 50:
                error_message['recipient_company'] = 'Recipient Company must be Minimum 50 Char'
            elif len(customer.recipient_company) < 2:
                error_message['recipient_company'] = 'Recipient Company must be 2 char long'

        if len(customer.recipient_vat_number) > 0:
            if len(customer.recipient_vat_number) > 25:
                error_message['recipient_vat_number'] = 'Recipient vat number Minimum 25 Char'
           

        if not customer.recipient_address:
            error_message['recipient_address'] = ' Recipient address is Required'
        elif len(customer.recipient_address) < 2:
            error_message['recipient_address'] = 'Recipient address name  must be 2 char long or more'
        elif len(customer.recipient_address) > 90:
            error_message['recipient_address'] = 'Recipient address Minimum 90 Char'

        if len(customer.recipient_apartment) > 0:
            if len(customer.recipient_apartment) > 20:
                error_message['recipient_apartment'] = 'Sender apartment suit Minimum 20 Char'
         

        if not customer.recipient_city:
            error_message['recipient_city'] = ' Recipient city is Required'
       
        elif len(customer.recipient_city) > 45:
            error_message['recipient_city'] = 'Recipient city  Minimum 45 Char'

        if not customer.recipient_country:
            error_message['recipient_country'] = "Recipient Country Name Required !!"
        elif len(customer.recipient_country) < 2:
            error_message['recipient_country'] = 'Recipient Country  must be 2 char long or more'
        elif len(customer.recipient_country) > 56:
            error_message['recipient_country'] = 'Recipient Country  Name Minimum 56 Char'

        if len(customer.recipient_province) > 0:
            if len(customer.recipient_province) > 56:
                error_message['recipient_province'] = 'Recipient province  Minimum 56 Char'
           

        if not customer.recipient_postal_code:
            error_message['recipient_postal_code'] = ' Recipient postal code is Required'
       
        elif len(customer.recipient_postal_code) > 12:
            error_message['recipient_postal_code'] = 'Recipient Postal code  Minimum 12 Char'

        if len(customer.recipient_phone) > 0:
            if len(customer.recipient_phone) > 15:
                error_message['recipient_phone'] = 'Recipient Phone number Minimum 15 Char'
           

        return error_message


class SuccessView(TemplateView):
    def get(self, request, **kwargs):

        data = Customer.objects.last()
        data = data.__dict__
        html_body = render_to_string("orders/order_form_show_data.html", {'data': data})
        data['web_type'] = 'html'
        message = EmailMultiAlternatives(
            "Payment Data",
            html_body,
            'santosh.zestgeek@gmail.com',
            [data['email']],
        )
        message.attach_alternative(html_body, "text/html")
        message.send()
        if message:
            print("Mail Sent")
        else:
            print("Mail Not Sent")
        return render(request, "orders/order_form_show_data.html", {'data': data})


class CancelView(TemplateView):
    template_name = "orders/cancel.html"


@method_decorator(
    csrf_exempt, name="dispatch"
)
class WebhookView(View):
    def post(self, request):
        payload = request.body
        print(payload)
        event = None

        try:
            event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
        except ValueError as e:
            return HttpResponse(status=400)

        if event.type == "payment_intent.succeeded":
            payment_intent = event.data.object
            print(request.session["parcel"])
            for key, value in request.session.items():
                print("{} => {}".format(key, value))
            print_label(request, payload)
            print("PaymentIntent was successful!")
        elif event.type == "payment_method.attached":
            payment_method = event.data.object
            print("PaymentMethod was attached to a Customer!")
        else:
            print("Unhandled event type {}".format(event.type))
        print("striped")

        return HttpResponse(status=200)


def print_label(request, payload):
    """req = request.POST
    sdr_name = req.get("sender-first-name", "") + req.get("sender-last-name", "")
    rec_name = req.get("recipient-first-name", "") + req.get("recipient-last-name", "")
    parcel = request.session["parcel"]
    rate = request.session["final_rate"]
    all_rates = request.session["all"]
    body = {
        "shipper": {
            "postal_code": req.get("sender-postal-code", ""),
            "city": req.get("sender-city"),
            # "federal_tax_id": "string",
            # "state_tax_id": "string",
            "person_name": sdr_name,
            "company_name": req.get("sender-company", ""),
            "country_code": req.get("sender-country", ""),
            "email": req.get("sender-email", ""),
            "phone_number": req.get("sender-phone", ""),
            # "state_code": "string",
            # "suburb": "string",
            # "residential": False,
            "address_line1": req.get("address", ""),
            # "address_line2": "string",
            # "validate_location": False,
        },
        "recipient": {
            "postal_code": req.get("recipient-postal-code", ""),
            "city": req.get("recipient-city", ""),
            # "federal_tax_id": "string",
            # "state_tax_id": "string",
            "person_name": rec_name,
            "company_name": req.get("recipient-company", ""),
            "country_code": req.get("recipient-country", ""),
            "email": req.get("recipient-email", ""),
            "phone_number": req.get("recipient-phone", ""),
            # "state_code": "string",
            # "suburb": "string",
            # "residential": false,
            "address_line1": req.get("recipient-address", ""),
            # "address_line2": "string",
            # "validate_location": False,
        },
        "parcels": [
            {
                "weight": parcel.weight,
                "width": parcel.width,
                "height": parcel.height,
                "length": parcel.length,
                # "packaging_type": "string",
                # "package_preset": "string",
                "description": "",
                "content": req.get("parcel-content", ""),
                "is_document": "",
                "weight_unit": "KG",
                "dimension_unit": "CM",
            }
        ],
        "options": {},
        "payment": {"paid_by": "sender", "currency": "EUR", "account_number": ""},
        "customs": {
            "aes": "",
            "eel_pfc": "",
            "content_type": "",
            "content_description": "",
            "incoterm": "",
            "commodities": [
                {
                    "id": "string",
                    "weight": 0,
                    "weight_unit": "KG",
                    "description": "string",
                    "quantity": 0,
                    "sku": "string",
                    "value_amount": 0,
                    "value_currency": "string",
                    "origin_country": "string",
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
                    "residential": false,
                    "address_line1": "string",
                    "address_line2": "string",
                    "validate_location": false,
                    "validation": {"success": true, "meta": {}},
                },
            },
            "invoice": "string",
            "invoice_date": "string",
            "commercial_invoice": true,
            "certify": true,
            "signer": "string",
            "certificate_number": "string",
            "options": {},
        },
        "reference": "string",
        "label_type": "PDF",
        "selected_rate_id": rate["id"],
        "rates": [all_rates],
    }
    print(body)
    data = body
    url = ""
    headers = {
        "Authorization": "Token key_61216ff961b3df111e8fbeed4cadd342",
        "Content_type": "application/json",
    }
    response = requests.post(f"{ url }/v1/proxy/shipping", headers=headers, json=data)
    r = response.json()
    print(json.dumps(r, indent=2))
    order = Orders()
    order.shipment_id = "1234"
    order.status = True
    order.amount = "123"
    order.stripe_payment_intent = payload["id"]"""
    return HttpResponse(status=200)


def trackingPage(request):
    return render(request, 'components/tracking_page.html')


def requestPurplship(url, method="GET", data={}):
    if method == 'POST':
        tokenResponse = requests.post(url, data)
    else:
        tokenResponse = requests.get(url)
    tokenResponse.headers['content-type']
    'application/json; charset=utf8'
    jsonResonse = tokenResponse.json()

    return jsonResonse


def api(request):
    url = "http://163.172.155.26:5002/api/token"
    data = {
        "email": "demo@example.com",
        "password": "Gozagel123"
    }
    apiResponse = requestPurplship(url, 'POST', data)
    if apiResponse:
        refreshToken = apiResponse.get('refresh')
        print('first time refreshToken', refreshToken)
        accessTokens = apiResponse.get('access')

        # verify token

        VerifyTokenUrl = "http://163.172.155.26:5002/api/token/verify"
        data = {
            "token": accessTokens
        }
        verifyApi = requestPurplship(VerifyTokenUrl,'POST', data)

        RefreshToken = "http://163.172.155.26:5002/api/token/refresh"
        data_ref = {
            "refresh": refreshToken
        }
        RefreshTokens = requestPurplship(RefreshToken, 'POST', data_ref)
        print('RefreshTokens=============', RefreshTokens)
        request.session['RefreshToken'] = RefreshTokens

    return HttpResponse(True if RefreshTokens else False)


def finddickeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in finddickeys(i, kv):
                yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in finddickeys(j, kv):
                yield x


def tracking_data(request):
    if request.method == 'POST':
        trackingID = request.POST['lname']
        url = f"http://163.172.155.26:5002/v1/proxy/tracking/fedex/{trackingID}"

        user_token = request.session.get('RefreshToken')
        print('your user token data ',user_token)
        Verify_token = user_token.get('access')
        print('Verify_token======', Verify_token)
        payload = ""
        headers = {
            'Content-Type': 'json_pretty,application/json',
            'Authorization': 'Bearer {}'.format(Verify_token),
            'Cookie': 'csrftoken=hQwfEGJFkpBXuJlvujQ2Es4GgaH1qT5s1VSrPogdXZ3nLv8WVQ5FOEKhBTpOpTeM'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        json_object = response.json()

        print("JSON OBJECT=======", type(json_object))
        carrier_name = list(finddickeys(json_object, 'carrier_name'))
        carrier_id = list(finddickeys(json_object, 'carrier_id'))
        tracking_number = list(finddickeys(json_object, 'tracking_number'))
        delivered = list(finddickeys(json_object, 'delivered'))
        status = list(finddickeys(json_object, 'status'))
        date = list(finddickeys(json_object, 'date'))

        message = list(finddickeys(json_object, 'message'))
        print("message", message)
        if not message:
            message = ""
        else:
            message = message[0]
        code = list( finddickeys(json_object, 'code'))
        isTokenEroor = False
        if code[1] == "token_not_valid":
            isTokenEroor = True
        context = {
            'carrier_name':carrier_name,
            'carrier_id':carrier_id,
            'tracking_number':tracking_number,
            'delivered':delivered,
            'status':status,
            'json_object':json_object,
            'isTokenEroor': isTokenEroor,
            'message': message
        }

        return render(request, 'components/tracking_data.html', context)

    else:
        return render(request, 'components/tracking_page.html')


