import unittest
from question24 import kth_largest

class TestKthLargest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(kth_largest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(kth_largest([7,10,4,3,20,15], 3), 10)
        self.assertEqual(kth_largest([1,2,3], 1), 3)

if __name__ == "__main__":
    unittest.main()
