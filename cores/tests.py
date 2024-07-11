from django.test import TestCase, Client
from django.urls import reverse
import json

class OrderAPITest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_order_success(self):
        response = self.client.post(reverse('api_orders'), json.dumps({
            "id": "1",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "666",
            "currency": "TWD"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_order_failure(self):
        response = self.client.post(reverse('api_orders'), json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
