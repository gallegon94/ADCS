import unittest
import math


class TestConverter(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(math.ceil(5.1), 6)

    def test_upper(self):
        self.assertEqual(math.ceil(5.9), 6)

    def test_invalid_number(self):
        with self.assertRaises(TypeError):
            math.ceil(None)

    def test_negative(self):
        self.assertEqual(math.ceil(-1.5), -1)

    def test_manual(self):
        number = 4.9
        self.assertEqual(math.ceil(number), number - (number % 1) + 1)
