
from urllib import response
from django.test import TestCase,RequestFactory
from django.urls import reverse,resolve
from .models import Customer, Search
from .views import BookView, CheckoutView, SuccessView
from django.urls import reverse
class TestCategory(TestCase):
    def test_category(self):
        category = Search.objects.create(address='Test Category')
        self.assertEqual(str(category), 'Test Category')

class Testview(TestCase):
    def setUp(self):
        self.register_url=reverse('checkout')
        self.tracking=reverse('trackingPage')
        self.user={
            'Firstname':'first_name',
            'last':'last_name',
            'email':'shivam@gmail.com',
            'parcel':'parcel',
            'value':'value',
            'sender-first-name':'sender-first-name',
            'sender-last-name':'sender-last-name',
            'sender-email':'rahul@gmail.com',
            'sender-company':'sender-company',
            'sender-tax':' sender_vat_number',
            'sender-address':'address',
            'sender-apartment':'sender-apartment',
            'sender-city':'sender-city',
            'sender-country':'sender-country',
            'sender-province':'sender-province',
            'sender-postal-code':'sender-postal-code',
            'sender-phone':'sender-phone',
            'recipient-first-name':'recipient-first-name',
            'recipient-last-name':'recipient-last-name',
            'recipient-email':'shivam@gmail.com',
            'recipient-company':'recipient-company',
            'recipient-tax':'recipient-tax',
            'recipient-address':'recipient-address',
            'recipient-apartment':'recipient-apartment',
            'recipient-city':'recipient-city',
            'recipient-countrye':'recipient-countrye',
            'recipient-province':'recipient-province',
            'recipient-postal-code':'recipient-postal-code',
            'recipient-phone':'recipient-phone'
        }
        self.user_validations={
            'Firstname':'',
            'last':'',
            'email':'',
            'parcel':'',
            'value':'',
            'sender-first-name':'',
            'sender-last-name':'',
            'sender-email':'ram',
            'sender-company':'u',
            'sender-tax':'gdgdgdgdgdggdgddggdgdgdgdgdggdgdgdgdgdgdgdg',
            'sender-address':'',
            'sender-apartment':'hshshshshhshshshshshshhshshshshshshshs',
            'sender-city':'',
            'sender-country':'',
            'sender-province':'gsggsgsgsgsgsggsgsgsggsgsgsggsggsgsggsggsgsggsgsgsgsgsggsgsgsggsgsggs',
            'sender-postal-code':'',
            'sender-phone':'727272772727277272772',
            'recipient-first-name':'',
            'recipient-last-name':'',
            'recipient-email':'sh',
            'recipient-company':'r',
            'recipient-tax':'ggdgdgdgdggdgdggdgdggdggdgdgdgdggdgdgdgdggdgdgd',
            'recipient-address':'',
            'recipient-apartment':'rggggggxgxgxgxgxggxgxggxgxg',
            'recipient-city':'',
            'recipient-countrye':'',
            'recipient-province':'hbhyyhhyhhhhuhdhdhdhdhhdhhdhddhhdhdhhdhdhdhdhdhhdhdhdhdhdhdhdhddhdhdhdhdhduhwhuuhuhhuuhhuuhhu',
            'recipient-postal-code':'',
            'recipient-phone':'99999999999999999999999'
        }
        self.user_check_validations={
            'Firstname':'f',
            'last':'l',
            'email':'sh',
            'parcel':'gdgdgdgdgdggdgdgdgdgdggdhhhhgdggdgdgdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgghhhhhhhdhdhdhdhhdhdhdhhdhdhdhhdhdhdhhdhdhdhdhhdgdgdgdgdggdgdgdgdgdggdgdggdgdgdggdgdggdgdgdggdgdgdgdggdgdgdggdgdgggdgdgdggdgdgdgggggdgdgdggdgdgdgdgdgdgdgdgdggd',
            'value':'valuehhggggg',
            'sender-first-name':'s',
            'sender-last-name':'s',
            'sender-email':'gdggdgdgdgdgdggdgdgdggdgdgdgdggdgdgdgdggdgdgdggdgdgdgdgdggdgdgdgdgdggdhhhhgdggdgdgdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgghhhhhhhdhdhdhdhhdhdhdhhdhdhdhhdhdhdhhdhdhdhdhhdgdgdgdgdggdgdgdgdgdggdgdggdgdgdggdgdggdgdgdggdgdgdgdggdgdgdggdgdgggdgdgdggdgdgdgggggdgdgdggdgdgdgdgdgdgdgdgdggd',
            'sender-company':'hdhhdhdhdhdhdhhdhdhdhhdhdhdhdhhdhdhdhdhhdhdhdhdhhdhdhhdhdhdhhdhdhdhdhhdhdhdhdhhdhdhdhhdhdhdhdhhdhdhdhdhdh',
            'sender-tax':'',
            'sender-address':'d',
            'sender-apartment':'',
            'sender-city':'senderhhhhhhhhhdhdhdhhdhdhdhdhdhhdhdhdhhdhdhdhdhdhhdhdhdhdhhdhdhdhdhddh',
            'sender-country':'s',
            'sender-province':'',
            'sender-postal-code':'',
            'sender-phone':'',
            'recipient-first-name':'r',
            'recipient-last-name':'r',
            'recipient-email':'gdgdgdgdgdggdgdgdgdgdggdhhhhgdggdgdgdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgghhhhhhhdhdhdhdhhdhdhdhhdhdhdhhdhdhdhhdhdhdhdhhdgdgdgdgdggdgdgdgdgdggdgdggdgdgdggdgdggdgdgdggdgdgdgdggdgdgdggdgdgggdgdgdggdgdgdgggggdgdgdggdgdgdgdgdgdgdgdgdggd',
            'recipient-company':'recipientHDHHDHHDHDHDHHDHDHDHHDHDHDHUDHUDUHDHUHUDHUDHUUHDHUWHUHUWHUWUHWHUHUWDHUDWUHUDHWUHDWHUDWHUDHWUUHWHUDWUHDWHUDWUHHUDUHWHUWUHWUHHUW',
            'recipient-tax':'',
            'recipient-address':'r',
            'recipient-apartment':'r',
            'recipient-city':'recipient-cithdhduuhdhuhuehuedehudehudeuhdehudehuedhudeeduduheduhdeuhdehudedeuduhdeuhdehudeuhedhuy',
            'recipient-countrye':'r',
            'recipient-province':'',
            'recipient-postal-code':'',
            'recipient-phone':''
        }
        self.user_max={
            'Firstname':'hdhdhdhhdhhdhdhhdhhdhdhdhuhhuhuhuhuhuuhuhhudhudhuduhuhduhdhudhudhudhuduhhduhuduhduhdhuduhduh',
            'last':'dhuduhhdududuhdhuhuduhdhudhudhuhudhudhudhuduhhudhudhudhuudhhudhuduhhudhuduhdhudhuhuduhduhdhu',
            'email':'gdgdgdgdgdggdgdgdgdgdggdhhhhgdggdgdgdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgdggdgdgdgghhhhhhhdhdhdhdhhdhdhdhhdhdhdhhdhdhdhhdhdhdhdhhdgdgdgdgdggdgdgdgdgdggdgdggdgdgdggdgdggdgdgdggdgdgdgdggdgdgdggdgdgggdgdgdggdgdgdgggggdgdgdggdgdgdgdgdgdgdgdgdggd',
            'parcel':'parcel',
            'value':'value',
            'sender-first-name':'shhfhhfhfhhfhfhfhfhfhfuhfhuhfuhufhufhufhuhurhurhuruhfrhuhufruhrfhufrhfrhurfhurfhufrhurfhurfhurfurfuhr',
            'sender-last-name':'bhhhhbhdhhdhdhudehuduhedhuduhedhudehueddeuedhudehuehdeuhdehdedehueduhdeuhedhueuhedhudhuhduheduhduedhhuhuedhudeue',
            'sender-email':'rahul@gmail.com',
            'sender-company':'sender-company',
            'sender-tax':' sender_vat_number',
            'sender-address':'ghejrghjerghjrhegjrgrhjgherhjwegrhjghrehgghjrehjerwghrejhgrewhgrewhejgrhjgerrghejwgehrjwgrewhjrehjwhreghejwhegwhgrewhgeghewghwehgrhgrhghwejghjrewhgjwhjwehgjrewhjgrgjhwergjhwegrjhwegrjhwegrjhwgejrhgwejhrgjhwegrhjwe',
            'sender-apartment':'sender-apartment',
            'sender-city':'sender-city',
            'sender-country':'gggeydyeydgyegydgyedegyegydygdeygedgydegyedgedygdeygdegyeddygdeygedgydeedgdgbeddebbdbdbdbdbdbbdbdbdhbdydydydydyyeeydydeydeybdeybdeybedyebd',
            'sender-province':'sender-province',
            'sender-postal-code':'sender-postal-code',
            'sender-phone':'sender-phone',
            'recipient-first-name':'rgggeydyeydgyegydgyedegyegydygdeygedgydegyedgedygdeygdegyeddygdeygedgydeedgdgbeddebbdbdbdbdbdbbdbdbdhbdydydydydyyeeydydeydeybdeybdeybedyebd',
            'recipient-last-name':'recipient-last-namegggeydyeydgyegydgyedegyegydygdeygedgydegyedgedygdeygdegyeddygdeygedgydeedgdgbeddebbdbdbdbdbdbbdbdbdhbdydydydydyyeeydydeydeybdeybdeybedyebd',
            'recipient-email':'shivam@gmail.com',
            'recipient-company':'recipient-company',
            'recipient-tax':'recipient-tax',
            'recipient-address':'recipient-addressgggeydyeydgyegydgyedegyegydygdeygedgydegyedgedygdeygdegyeddygdeygedgydeedgdgbeddebbdbdbdbdbdbbdbdbdhbdydydydydyyeeydydeydeybdeybdeybedyebd',
            'recipient-apartment':'recipient-apartment',
            'recipient-city':'recipient-city',
            'recipient-countrye':'recipient-countryegggeydyeydgyegydgyedegyegydygdeygedgydegyedgedygdeygdegyeddygdeygedgydeedgdgbeddebbdbdbdbdbdbbdbdbdhbdydydydydyyeeydydeydeybdeybdeybedyebd',
            'recipient-province':'recipient-province',
            'recipient-postal-code':'recipient-postal-code',
            'recipient-phone':'recipient-phone'

        }

class Demoview(Testview):
  
    def test_view(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'orders/book.html')

    def test_view_post(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)

    def test_validation_required(self):
        response=self.client.post(self.register_url,self.user_validations,format='text/html')
        self.assertEqual(response.status_code,200)

    def test_minimum_char(self):
        response=self.client.post(self.register_url,self.user_check_validations,format='text/html')
        self.assertEqual(response.status_code,200)

    def test_max_char(self):
        response=self.client.post(self.register_url,self.user_max,format='text/html')
        self.assertEqual(response.status_code,200)

    def test_tracking(self):
        response=self.client.get(self.tracking)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'components/tracking_page.html')

        

        





