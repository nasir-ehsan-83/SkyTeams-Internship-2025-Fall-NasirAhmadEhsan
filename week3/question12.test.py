import unittest
from question12 import is_palindrome

class TestQuestion12(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(123))

if __name__ == "__main__":
    unittest.main()
