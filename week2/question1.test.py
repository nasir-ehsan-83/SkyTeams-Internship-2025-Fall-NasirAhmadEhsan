import unittest
from question1 import swap

class TestQuestion1(unittest.TestCase):
    def test_swap(self):
        self.assertEqual(swap(5, 10), (10, 5))
        self.assertEqual(swap(0, -1), (-1, 0))

if __name__ == "__main__":
    unittest.main()
