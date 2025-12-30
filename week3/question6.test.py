import unittest
from question6 import smallest

class TestQuestion6(unittest.TestCase):
    def test_smallest(self):
        self.assertEqual(smallest([4,7,1,9,2]), 1)
        self.assertEqual(smallest([]), None)

if __name__ == "__main__":
    unittest.main()
