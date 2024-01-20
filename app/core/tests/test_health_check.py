"""
Test For the Health Check API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTest(TestCase):
    """Test the Health Check API."""

    def test_health_check(self):
        """Test the Health Check API."""
        clint = APIClient()
        url = reverse('health-check')
        res = clint.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
