from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTestst(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating user with an email is successful
        """
        email = 'test2020@google.com'
        password = "password123"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        