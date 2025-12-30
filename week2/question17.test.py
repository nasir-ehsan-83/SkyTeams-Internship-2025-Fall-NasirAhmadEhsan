import unittest
from question17 import sum_natural

class TestQuestion17(unittest.TestCase):
    def test_sum_natural(self):
        self.assertEqual(sum_natural(5), 15)
        self.assertEqual(sum_natural(10), 55)

if __name__ == "__main__":
    unittest.main()
