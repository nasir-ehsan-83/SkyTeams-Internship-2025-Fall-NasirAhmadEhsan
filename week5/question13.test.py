import unittest
from question13 import backspaceCompare

class TestBackspaceCompare(unittest.TestCase):
    def test_backspace(self):
        self.assertTrue(backspaceCompare("ab#c", "ad#c"))
        self.assertTrue(backspaceCompare("a##c", "#a#c"))
        self.assertFalse(backspaceCompare("a#c", "b"))

if __name__ == "__main__":
    unittest.main()
