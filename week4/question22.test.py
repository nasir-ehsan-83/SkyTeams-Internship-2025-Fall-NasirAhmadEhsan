import unittest
from question22 import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(merge_intervals([[1,3],[2,6],[8,10]]), [[1,6],[8,10]])
        self.assertEqual(merge_intervals([[1,4],[4,5]]), [[1,5]])
        self.assertEqual(merge_intervals([]), [])

if __name__ == "__main__":
    unittest.main()
