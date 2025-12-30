import unittest
from question24 import gcd

class TestQuestion24(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12,18), 6)
        self.assertEqual(gcd(7,5), 1)

if __name__ == "__main__":
    unittest.main()
