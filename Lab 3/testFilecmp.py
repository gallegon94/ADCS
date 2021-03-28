import unittest
import filecmp
import os
from os.path import dirname, abspath


class TestCFileCmp(unittest.TestCase):
    def test_equal(self):
        file_a = os.path.join(dirname(abspath(__file__)), "resources", "same1")
        file_b = os.path.join(dirname(abspath(__file__)), "resources", "same2")
        self.assertTrue(filecmp.cmp(file_a, file_b))

    def test_diff(self):
        file_a = os.path.join(dirname(abspath(__file__)), "resources", "same1")
        file_b = os.path.join(dirname(abspath(__file__)), "resources", "diff")
        self.assertFalse(filecmp.cmp(file_a, file_b))

    def test_none(self):
        file_a = os.path.join(dirname(abspath(__file__)), "resources", "missing")
        file_b = os.path.join(dirname(abspath(__file__)), "resources", "diff")
        with self.assertRaises(FileNotFoundError):
            self.assertFalse(filecmp.cmp(file_a, file_b))
