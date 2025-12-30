import unittest
from question7 import sum_array

class TestQuestion7(unittest.TestCase):
    def test_sum_array(self):
        self.assertEqual(sum_array([1,2,3,4,5]), 15)
        self.assertEqual(sum_array([]), 0)

if __name__ == "__main__":
    unittest.main()
