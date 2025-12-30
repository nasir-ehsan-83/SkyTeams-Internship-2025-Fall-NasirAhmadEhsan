import unittest
from question2 import merge_sorted_arrays

class TestMergeSortedArrays(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(merge_sorted_arrays([1,3,5],[2,4,6]), [1,2,3,4,5,6])
        self.assertEqual(merge_sorted_arrays([], [1,2]), [1,2])
        self.assertEqual(merge_sorted_arrays([1,2], []), [1,2])
        self.assertEqual(merge_sorted_arrays([], []), [])

if __name__ == "__main__":
    unittest.main()
