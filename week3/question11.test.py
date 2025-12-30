import unittest
from question11 import primes_up_to

class TestQuestion11(unittest.TestCase):
    def test_primes_up_to(self):
        self.assertEqual(primes_up_to(10), [2,3,5,7])
        self.assertEqual(primes_up_to(1), [])

if __name__ == "__main__":
    unittest.main()
