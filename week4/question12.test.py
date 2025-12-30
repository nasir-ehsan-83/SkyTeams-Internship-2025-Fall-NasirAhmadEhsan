import unittest
from question12 import char_frequency

class TestCharFrequency(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(char_frequency("banana"), {'b':1,'a':3,'n':2})
        self.assertEqual(char_frequency(""), {})
        self.assertEqual(char_frequency("aa"), {'a':2})

if __name__ == "__main__":
    unittest.main()
