import unittest
from question2 import largest_smallest

class TestQuestion2(unittest.TestCase):
    def test_largest_smallest(self):
        self.assertEqual(largest_smallest(3, 9, 5), (9, 3))
        self.assertEqual(largest_smallest(-1, -5, 0), (0, -5))

if __name__ == "__main__":
    unittest.main()
