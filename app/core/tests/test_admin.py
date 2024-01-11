"""
Test fo Admin
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import client


class AdminTest(TestCase):
    """Test for Django Admin."""

    def setUp(self):
        """Create user and client"""
        self.client = client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpassword123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpassword123',
        )

    def test_users_list(self):
        """Test that users are listed on the page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)