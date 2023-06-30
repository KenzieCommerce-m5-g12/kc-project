from django.test import TestCase
from cart.models import Cart


class CartModelTest(TestCase):
    def test_products_properties(self):
        result = Cart._meta.get_field("products")
        msg = f"Make sure the products property is coming with the correct values"
        self.assertEqual(result, msg)

    def test_userId_properties(self):
        result = Cart._meta.get_field("user_id")
        msg = f"Make sure the user_id property is coming with the correct user values"
        self.assertEqual(result, msg)
