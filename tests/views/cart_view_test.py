from rest_framework.test import APITestCase
from rest_framework.views import status


class CartViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.BASE_URL = "/api/cart/"

    def test_create_cart_success(self):
        product = {"product_id": 1}

        response = self.client.post(self.BASE_URL, data=product, format="json")
        expected_stats_code = status.HTTP_201_CREATED
        msg = f"Check if the expected status code is {expected_stats_code}"
        self.assertEquals(expected_stats_code, response.status_code, msg)

        expected_response_data = {
            "id": 1,
            "name": "PC gamer boladão",
            "category": "eletronicos",
            "url": "http://image.png",
            "price": 4999.99,
            "user": {
                "id": 1,
                "name": "vinicius",
                "email": "vinicius@mail.com",
            },
        }

        response_data = response.json()
        self.assertDictEqual(expected_response_data, response_data)

    def test_create_cart_without_required_fields(self):
        cart_data = {
            "id": 1,
            "name": "PC gamer boladão",
            "category": "eletronicos",
            "url": "http://image.png",
            "price": 4999.99,
            "user": {
                "id": 1,
                "name": "vinicius",
                "email": "vinicius@mail.com",
            },
        }

        response = self.client.post(self.BASE_URL, data=cart_data, format="json")
        expected_stats_code = status.HTTP_400_BAD_REQUEST
        msg = f"Check if the expected status code is 201, you receive 400"
        self.assertEquals(expected_stats_code, response.status_code, msg)

    def test_list_cart_success(self):
        cart_count = 10
        response = self.client.get(self.BASE_URL)
        expected_count = cart_count
        result_count = len(response.json())

        msg = f"make sure item returns are coming correctly"
        self.assertEqual(result_count, expected_count, msg)
