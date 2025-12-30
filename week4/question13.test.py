import unittest
from question13 import pattern_match

class TestPatternMatch(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(pattern_match("abba","dog cat cat dog"))
        self.assertFalse(pattern_match("abba","dog cat cat fish"))
        self.assertFalse(pattern_match("abc","dog cat cat"))

if __name__ == "__main__":
    unittest.main()
