import unittest
from question15 import max_subarray_sum

class TestMaxSubarraySum(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(max_subarray_sum([1,2,3]), 6)
        self.assertEqual(max_subarray_sum([-1,-2,-3]), -1)
        self.assertEqual(max_subarray_sum([]), 0)

if __name__ == "__main__":
    unittest.main()
