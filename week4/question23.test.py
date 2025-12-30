import unittest
from question23 import top_k_frequent

class TestTopKFrequent(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(top_k_frequent([1,1,1,2,2,3],2), [1,2])
        self.assertEqual(top_k_frequent([4,4,4,6,6,7],1), [4])
        self.assertEqual(top_k_frequent([],1), [])

if __name__ == "__main__":
    unittest.main()
