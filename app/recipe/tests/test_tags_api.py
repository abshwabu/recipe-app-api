"""
Tests for the tags API.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from recipe.serializers import TagSerializer

TAG_URL = reverse('recipe:tag-list')


def create_user(**params):
    """Create a new user."""
    return get_user_model().objects.create_user(**params)