import requests
import json
from django.shortcuts import render
from django.views.generic import TemplateView, View
from core.views import generate_token, API_BASE_URL, PARCEL_ENDPOINT, USERNAME, PASSWORD, custom_response


no_postal_countries = [
    """These countries are notorious for not/barely using postal codes when it comes to delivery, this is why couriers don't always need these postal codes to provide rates"""
    "AO",
    "AG",
    "AW",
    "SH",
    "BS",
    "BZ",
    "BJ",
    "BW",
    "BO",
    "BQ",
    "BF",
    "BI",
    "CM",
    "CF",
    "KM",
    "CG",
    "CD",
    "CK",
    "CI",
    "CW",
    "DJ",
    "DM",
    "GQ",
    "ER",
    "FJ",
    "TF",
    "GM",
    "GA",
    "GH",
    "GD",
    "GY",
    "HM",
    "HK",
    "EG",
    "KI",
    "LY",
    "MO",
    "MW",
    "ML",
    "MR",
    "NR",
    "AN",
    "NU",
    "KP",
    "QA",
    "RW",
    "KN",
    "ST",
    "SC",
    "SL",
    "SB",
    "SR",
    "SY",
    "TL",
    "TG",
    "TK",
    "TO",
    "TV",
    "UG",
    "AE",
    "VU",
    "YE",
    "ZW",
]


class QuoteLogInView(TemplateView):
    template_name = "rates/quote_login.html"


class QuoteView(View):
    def get(self, request):
        token = generate_token(USERNAME, PASSWORD)
        hed = {"Authorization": f"Bearer {token.get('access')}"}
        api = f"{API_BASE_URL}{PARCEL_ENDPOINT}"
        print(request.GET["country-from"])
        weight = int(request.GET["weight"])
        width = int(request.GET["width"])
        height = int(request.GET["height"])
        length = int(request.GET["length"])
        country_to = request.GET["country-to"]
        city_from = request.GET["city-from"]
        city_to = request.GET["city-to"]
        country_from = request.GET["country-from"]
        key = "lRYjgaQQXR7LszBDX49cR19s9WalIQOuYl9eF7aiRdg"

        if country_from in no_postal_countries:
            postal_code_from = ""
        else:
            res = requests.get(
                f"https://geocode.search.hereapi.com/v1/geocode?q={city_from}+{country_from}&apiKey={key}"
            )
            resp = res.json()
            postal_code_from = resp["items"][0]["address"]["postalCode"]
            city_from = resp["items"][0]["address"]["city"]

        if country_to in no_postal_countries:
            postal_code_to = ""
        else:

            res = requests.get(
                f"https://geocode.search.hereapi.com/v1/geocode?q={city_to}+{country_to}&apiKey={key}"
            )
            resp = res.json()
            postal_code_to = resp["items"][0]["address"]["postalCode"]
            city_to = resp["items"][0]["address"]["city"]

        parcel = {
            "weight": weight,
            "width": width,
            "height": height,
            "length": length,
            "from": country_from,
            "postal_code_from": postal_code_from,
            "city_from": city_from,
            "city_to": city_to,
            "to": country_to,
            "postal_code_to": postal_code_to,
        }
        body = {
            "options": {},
            "parcels": [
                {
                "dimension_unit": "CM",
                "height": 2,
                "is_document": "false",
                "length": 2,
                "weight": 2,
                "weight_unit": "KG",
                "width": 2
                }
            ],
            "recipient": {
                "city": "Paris",
                "country_code": "FR",
                "postal_code": "75001",
                "residential": "true"
            },
            "shipper": {
                "city": "cairo",
                "country_code": "EG",
                "residential": "true"
            }
            }
        data = body
        url = "http://51.159.178.154:5002/v1"
        headers = {
            "Authorization": "Token key_d314031424e44537096092aad60dbb6f",
            "Content_type": "application/json",
        }
    
        response = requests.post(
            f"{ url }/proxy/rates", headers=hed, json=data
        )
        r = response.json()
        print(r)
        no_rates = False
        try:
            rates = [
                {
                    "id": rate["id"],
                    "carrier": rate["carrier_name"],
                    "carrier_id": rate["carrier_id"],
                    "currency": rate["currency"],
                    "rate": rate["total_charge"],
                    "delay": rate["transit_days"],
                }
                for rate in r["rates"]
            ]
        except KeyError as e:
            print(e)
            rates = {}
            no_rates = True
        request.session["all"] = json.dumps(r)
        request.session["rates"] = rates
        request.session["parcel"] = parcel
        print(request.session["parcel"])
        print(request.session["rates"])
        return render(
            request,
            context={"rates": rates, "parcel": parcel, "no_rates": no_rates},
            template_name="rates/quote.html",
        )
