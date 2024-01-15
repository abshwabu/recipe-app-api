"""
Test for Models.
"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


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

    def test_new_user_with_out_email_raises_error(self):
        """Test that creating a user without an email raises an ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='sample recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)
