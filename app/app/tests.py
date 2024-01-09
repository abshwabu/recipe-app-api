'''
Test
'''
from django.test import SimpleTestCase

from app import calc

class TestCalc(SimpleTestCase):
    """
    Test for calc
    """
    def test_add(self):
        """test adding number"""
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_subtract(self):
        res = calc.subtract(5,6)
        self.assertEqual(res,1)