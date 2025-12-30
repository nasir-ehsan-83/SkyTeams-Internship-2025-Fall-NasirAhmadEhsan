import unittest
from question14 import factorial

class TestQuestion14(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

if __name__ == "__main__":
    unittest.main()
