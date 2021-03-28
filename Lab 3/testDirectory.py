import unittest
from directory import Contact, Directory
import os
from os.path import dirname, abspath, isfile


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.file = "test.txt"
        self.dir = Directory(self.file)

    def tearDown(self):
        if isfile(self.file):
            os.remove(self.file)

    def test_equal(self):
        self.dir.add_contact("pepe", "juan@gmail.com", "27", "Mexico")
        contact = Contact("pepe", "juan@gmail.com", "27", "Mexico")
        self.assertEqual(contact, self.dir.search_by_email("juan@gmail.com"))

    def test_not_equal(self):
        self.dir.add_contact("pepe", "juan@gmail.com", "27", "Mexico")
        contact = Contact("juan", "jua@gmail.com", "27", "Mexico")
        self.assertNotEqual(contact, self.dir.search_by_email("jua@gmail.com"))

    def test_search_age(self):
        self.dir.add_contact("pepe", "pepe@gmail.com", "27", "Mexico")
        self.dir.add_contact("juan", "juan@gmail.com", "27", "Mexico")
        self.dir.add_contact("oscar", "oscar@gmail.com", "29", "Mexico")
        res = self.dir.search_by_age(27)
        for elem in res:
            self.assertEqual(elem._age, "27")

    def test_wrong_name(self):
        with self.assertRaises(ValueError):
            self.dir.add_contact("pepe2", "pepe@gmail.com", "27", "Mexico")

    def test_wrong_mail(self):
        with self.assertRaises(ValueError):
            self.dir.add_contact("pepe", "pepegmail.com", "27", "Mexico")

    def test_wrong_age(self):
        with self.assertRaises(ValueError):
            self.dir.add_contact("pepe", "pepe@gmail.com", "es", "Mexico")

    def test_wrong_country(self):
        with self.assertRaises(ValueError):
            self.dir.add_contact("pepe", "pepe@gmail.com", "27", "123")

    def test_check_file(self):
        self.dir.add_contact("pepe", "pepe@gmail.com", "27", "Mexico")
        self.dir.add_contact("juan", "juan@gmail.com", "27", "Mexico")
        self.dir.add_contact("oscar", "oscar@gmail.com", "29", "Mexico")
        self.dir.save()
        self.assertTrue(isfile(self.file))

    def test_load(self):
        self.dir.add_contact("pepe", "pepe@gmail.com", "27", "Mexico")
        self.dir.add_contact("juan", "juan@gmail.com", "27", "Mexico")
        self.dir.add_contact("oscar", "oscar@gmail.com", "29", "Mexico")
        self.dir.save()
        dir2 = Directory(self.file)
        self.assertEqual(self.dir.search_by_email("juan@gmail.com"), dir2.search_by_email("juan@gmail.com"))
