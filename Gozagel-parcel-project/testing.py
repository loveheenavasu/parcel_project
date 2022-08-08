from core.views import generate_token, API_BASE_URL,PARCEL_ENDPOINT, USERNAME, PASSWORD
import requests


def parcel_post(request):
    token = generate_token(USERNAME, PASSWORD)
    header = {"Authorization": f"Bearer {token.get('access')}"}
    api = f"{API_BASE_URL}{PARCEL_ENDPOINT}"
    data = {
          "weight":request.get('weight'),
          "width": request.get('width'),
          "height": request.get('height'),
          "length": request.get('length'),
          "packaging_type": request.get('packaging_type'),
          "package_preset": request.get('package_preset'),
          "description": request.get('description'),
          "content": request.get('content'),
          "is_document": request.get('is_document'),
          "weight_unit":request.get('weight_unit'),
          "dimension_unit": request.get('dimension_unit'),
          "items": [
            {
                "weight": request.get('weight'),
                "weight_unit": request.get('weight_unit'),
                "description": request.get('description'),
                "quantity": request.get('quantity'),
                "sku": request.get('sku'),
                "value_amount": request.get('value_amount'),
                "value_currency":request.get('value_currency'),
                "origin_country": request.get('origin_country'),
                "parent_id": request.get('parent_id'),
                }
  ],
  "reference_number": request.get('reference_number')
}
    req = requests.post(api,data=p,headers=header)
    data = req.json()
    print(request)
    print(data)
    return data



p = {
    "weight": 1.0,
    "width": 1.0,
    "height": 1.0,
    "length": 1.0,
    "packaging_type": "small_box",
    "package_preset": "string",
    "description": "birth card",
    "content": "card",
    "is_document": True,
    "weight_unit": "KG",
    "dimension_unit": "CM",
    "items": [
        {
            "weight": 1.0,
            "weight_unit": "KG",
            "description": "item string",
            "quantity": 1,
            "sku": "string",
            "value_amount": 0,
            "value_currency": "INR",
            "origin_country": "IND",
        }
    ],
    "reference_number": "123456789"
}
parcel_post(p)