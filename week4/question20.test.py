import unittest
from question20 import is_balanced

class TestBalancedParentheses(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_balanced("()[]{}"))
        self.assertFalse(is_balanced("(]"))
        self.assertTrue(is_balanced("{[()]}"))
        self.assertFalse(is_balanced("((("))

if __name__ == "__main__":
    unittest.main()
