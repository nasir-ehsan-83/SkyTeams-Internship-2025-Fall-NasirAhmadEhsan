import unittest
from question10 import is_prime

class TestQuestion10(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(1))

if __name__ == "__main__":
    unittest.main()
