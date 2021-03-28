import unittest
from findWords import count_words, get_file_content


class TestCounter(unittest.TestCase):
    def test_wc(self):
        ip = {"perro": 3, "gato": 1}
        self.assertEqual(count_words(["perro", "perro", "perro", "gato"]), ip)

    def test_empty(self):
        self.assertEqual(count_words([]), {})

    def test_invalid_file(self):
        with self.assertRaises(IOError):
            get_file_content("invalid.txt")

    def test_read_file(self):
        ip = ["aaaa", "qwe", "qwe", "perro", "perro", "perro"]
        self.assertEquals(get_file_content("test.txt"), ip)


if __name__ == '__main__':
    unittest.main()
