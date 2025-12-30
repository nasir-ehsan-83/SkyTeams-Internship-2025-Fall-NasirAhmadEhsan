import unittest
from question4 import swap

class TestQuestion4(unittest.TestCase):
    def test_swap(self):
        a, b = swap(5, 10)
        self.assertEqual((a, b), (10, 5))
        a, b = swap(-1, 1)
        self.assertEqual((a, b), (1, -1))

if __name__ == "__main__":
    unittest.main()
