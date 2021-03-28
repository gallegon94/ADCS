import unittest
from convert import int_to_str, str_to_int


class TestIntStr(unittest.TestCase):

    def test_datatype(self):
        self.assertTrue(isinstance(int_to_str(20), str))

    def test_20(self):
        self.assertEqual(int_to_str(20), "20")

    def test_5000(self):
        self.assertEqual(int_to_str(5000), "5000")

    def test_1500(self):
        self.assertEqual(int_to_str(1500), "1500")

    def test_3(self):
        self.assertEqual(int_to_str(3), "3")

    def test_5(self):
        self.assertEqual(int_to_str(5), "5")

    def test_1000000(self):
        self.assertEqual(int_to_str(1000000), "1000000")

    def test_0(self):
        self.assertEqual(int_to_str(0), "0")

    def test_negative_1000(self):
        self.assertEqual(int_to_str(-1000), "-1000")

    def test_invalid_type(self):
        with self.assertRaises(Exception):
            int_to_str("20")

    def test_negative(self):
        self.assertEqual(int_to_str(-20), "-20")


class TestStrInt(unittest.TestCase):
    def test_datatype_str(self):
        self.assertTrue(isinstance(str_to_int("20"), int))

    def test_20(self):
        self.assertEqual(str_to_int("20"), 20)

    def test_empty_str(self):
        with self.assertRaises(Exception):
            str_to_int("")

    def test_iinvalid_str(self):
        with self.assertRaises(Exception):
            str_to_int("20i")

    def test_invalid_type(self):
        with self.assertRaises(Exception):
            str_to_int(20)

    def test_negative(self):
        self.assertEqual(str_to_int("-20"), -20)

    def test_dnegative(self):
        with self.assertRaises(Exception):
            str_to_int("-2-0")

    def test_wrong_negative(self):
        with self.assertRaises(Exception):
            str_to_int("20-")

    def test_wrong_positive(self):
        with self.assertRaises(Exception):
            str_to_int("20+")

    def test_positive(self):
        self.assertEqual(str_to_int("+20"), 20)

    def test_0(self):
        self.assertEqual(str_to_int("0"), 0)
