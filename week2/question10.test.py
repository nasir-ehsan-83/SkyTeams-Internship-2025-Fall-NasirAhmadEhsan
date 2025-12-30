import unittest
from question10 import is_leap_year

class TestQuestion10(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2024))

if __name__ == "__main__":
    unittest.main()
