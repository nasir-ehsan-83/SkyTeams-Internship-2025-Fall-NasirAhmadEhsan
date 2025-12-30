import unittest
from question21 import longest_palindrome

class TestLongestPalindrome(unittest.TestCase):
    def test_cases(self):
        self.assertIn(longest_palindrome("babad"), ["bab","aba"])
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        self.assertEqual(longest_palindrome("a"), "a")
        self.assertEqual(longest_palindrome(""), "")

if __name__ == "__main__":
    unittest.main()
