'''
Test
'''
from django.test import SimpleTestCase

from .calc import add

class TestCalc(SimpleTestCase):
    """
    Test for calc
    """
    def test_add(self):
        """test adding number"""
        res = add(5,6)
        self.assertEqual(res,11)