from django.test import TestCase
from address.models import Address


class AddressModelTest(TestCase):
    def test_country_properties(self):
        expected = 40
        result = Address._meta_get_field("country").max_length
        msg = f"Check if the maximum length of country is {expected} characters"
        self.assertEqual(expected, result, msg)

        result = Address._meta.get_field("country").null
        msg = f"Make sure the `country` attribute is set to mandatory"
        self.assertFalse(result, msg)

    def test_state_properties(self):
        expected = 2
        result = Address._meta.get_field("state").max_length
        msg = f"Check if the maximum length of state is {expected} characters"
        self.assertEqual(expected, result, msg)

        result = Address._meta.get_field("state").null
        msg = f"Make sure the `state` attribute is set to mandatory"
        self.assertFalse(result, msg)

    def test_city_properties(self):
        expected = 40
        result = Address._meta.get_field("city").max_length
        msg = f"Check if the maximum length of city is {expected} characters"
        self.assertEqual(expected, result, msg)

        result = Address._meta.get_field("city").null
        msg = f"Make sure the `city` attribute is set to mandatory"
        self.assertFalse(result, msg)

    def test_road_properties(self):
        expected = 120
        result = Address._meta.get_field("road").max_length
        msg = f"Check if the maximum length of road is {expected} characters"
        self.assertEqual(expected, result, msg)

        result = Address._meta.get_field("road").null
        msg = f"Make sure the `road` attribute is set to mandatory"
        self.assertFalse(result, msg)

    def test_userId_properties(self):
        result = Address._meta.get_field("user_id")
        msg = f"Make sure the user_id property is coming with the correct user values"
        self.assertEqual(result, msg)

        result = Address._meta.get_field("user_id").null
        msg = f"Make sure the `user_id` attribute is set to mandatory"
        self.assertFalse(result, msg)
