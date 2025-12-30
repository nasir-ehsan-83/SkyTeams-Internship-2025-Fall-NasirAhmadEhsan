import unittest
from question4 import factors

class TestQuestion4(unittest.TestCase):
    def test_factors(self):
        self.assertEqual(factors(12), [1,2,3,4,6,12])
        self.assertEqual(factors(7), [1,7])

if __name__ == "__main__":
    unittest.main()
