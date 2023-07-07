from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):
    def test_username_properties(self):
        expected = 60
        result = User._meta.get_field("username").max_length
        msg = f"Check if the max_length is equal to {expected}"
        self.assertEqual(expected, result, msg)

    def test_email_properties(self):
        expected = 120
        result = User._meta.get_field("email").max_length
        msg = f"Check if the max_length is equal to {expected}"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("email").unique
        msg = f"Make sure the email is unique"
        self.assertTrue(result, msg)

    def test_password_properties(self):
        expected = 128
        result = User._meta.get_field("password").max_length
        msg = f"Check if the max_length is equal to {expected}"
        self.assertEqual(expected, result, msg)
