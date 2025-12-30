import unittest
from question23 import factorial_recursive

class TestQuestion23(unittest.TestCase):
    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(0), 1)

if __name__ == "__main__":
    unittest.main()
