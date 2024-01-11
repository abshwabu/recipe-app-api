"""
Test for Models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test Model."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'test@example.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for a new user"""
        sampleEmail = [
            ['test@Example.com', 'test@example.com'],
            ['test2@example.com', 'test2@example.com'],
            ['Test3@example.com', 'Test3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sampleEmail:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)
            
