from django.test import TestCase

from app.calc import add, subtract, multiply


class CalcTests(TestCase):

    def test_add_numbers(self):
        # Test that two numbers are added together
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        # Test subtract calc.
        self.assertEqual(subtract(1, 7), 6)

    def test_multiply_numbers(self):
        # yep
        self.assertEqual(multiply(2, 4), 8)
    