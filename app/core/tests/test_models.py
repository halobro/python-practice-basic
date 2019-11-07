from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Testing create new user with valid email"""
        email = 'user@gmail.com'
        password = 'weakpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email , email)
        self.assertTrue(user.check_password(password))
    
    def test_create_user_with_email_normalized(self):
        """Testing using normalized email"""
        email = "test@Gmail.com"
        password = "anotherweakpass123"

        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email.lower())