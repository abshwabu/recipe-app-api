"""
Test For the Health Check API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTest(TestCase):
    """Test the Health Check API."""
    