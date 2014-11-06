import unittest
from yourpackage import your_function


class TestYourModule(unittest.TestCase):
    def setUp(self):
        pass

    def test_your_function_zero(self):
        self.assertEqual(your_function(0), 2)

    def test_your_function_odd(self):
        self.assertEqual(your_function(1), 3)

    def test_your_function_greater_than_10000(self):
        self.assertEqual(your_function(10006), 8)

    def test_your_function_12345(self):
        self.assertEqual(your_function(12345), 17)
