import unittest
from question9 import isValid

class TestValidParentheses(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(isValid("()[]{}"))
        self.assertFalse(isValid("(]"))
        self.assertFalse(isValid("([)]"))
        self.assertTrue(isValid("{[]}"))

if __name__ == "__main__":
    unittest.main()
