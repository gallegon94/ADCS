import unittest
import sys
import convert2X
from convert2X import converter


class TestConverter(unittest.TestCase):
    def test_2(self):
        self.assertEqual(converter(2, 2), "10")
        self.assertEqual(converter(2, 16), "2")

    def test_10(self):
        self.assertEqual(converter(10, 2), "1010")
        self.assertEqual(converter(10, 16), "A")

    def test_16(self):
        self.assertEqual(converter(16, 2), "10000")
        self.assertEqual(converter(16, 16), "10")

    def test_17(self):
        self.assertEqual(converter(17, 2), "10001")
        self.assertEqual(converter(17, 16), "11")

    def test_120(self):
        self.assertEqual(converter(120, 2), "1111000")
        self.assertEqual(converter(120, 16), "78")

    def test_1024(self):
        self.assertEqual(converter(1024, 2), "10000000000")
        self.assertEqual(converter(1024, 16), "400")

    def test_1(self):
        self.assertEqual(converter(1, 2), "1")
        self.assertEqual(converter(1, 16), "1")

    def test_1994(self):
        self.assertEqual(converter(1994, 2), "11111001010")
        self.assertEqual(converter(1994, 16), "7CA")

    def test_negative(self):
        with self.assertRaises(BaseException):
            converter(-1, 2)

    def test_negative_base(self):
        with self.assertRaises(BaseException):
            converter(1, -2)
