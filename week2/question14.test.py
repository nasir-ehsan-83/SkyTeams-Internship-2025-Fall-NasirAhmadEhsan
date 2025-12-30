import unittest
from question14 import char_type

class TestQuestion14(unittest.TestCase):
    def test_char_type(self):
        self.assertEqual(char_type('a'), "Vowel")
        self.assertEqual(char_type('b'), "Consonant")
        self.assertEqual(char_type('5'), "Digit")
        self.assertEqual(char_type('#'), "Special")

if __name__ == "__main__":
    unittest.main()
