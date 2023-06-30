from django.test import TestCase
from products.models import Product


class ProductModelTest(TestCase):
    def test_name_properties(self):
        expected = 140
        result = Product._meta.get_field("name").max_length
        message = f"Verify if name field has less than {expected} characters"
        self.assertEqual(expected, result, message)

    def test_category_properties(self):
        expected = 20
        result = Product._meta.get_field("category").max_length
        message = (f"Verify if description field has less than {expected} characters.")
        self.assertEqual(expected, result, message)

    def test_price_properties(self):
        expected_max_digits = 8
        expected_max_decimal_places = 2
        message = f"Verify if max_digits and max_places properties are correct."

        result = Product._meta.get_field("price").max_digits
        self.assertLessEqual(expected_max_digits, result, message)

        result = Product._meta.get_field("price").decimal_places
        self.assertLessEqual(expected_max_decimal_places, result, message)

    def test_url_properties(self):
        expected = "TextField"
        result = Product._meta.get_field("url").get_internal_type()
        message = f"Verify if URL field is a TextField"
        self.assertEqual(result, expected, message)

    def test_description_properties(self):
        expected = "TextField"
        result = Product._meta.get_field("description").get_internal_type()
        message = f"Verify if DESCRIPTION field is a TextField"
        self.assertEqual(result, expected, message)

    def test_stock_properties(self):
        expected = "PositiveIntegerField"
        result = Product._meta.get_field("stock").get_internal_type()
        message = f"Verify if stock field has integer property"
        self.assertEqual(result, expected, message)

    # def test_user_properties(self):
    #     ...
