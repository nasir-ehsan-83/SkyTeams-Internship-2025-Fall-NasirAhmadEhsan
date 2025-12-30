import unittest
from question25 import set_zeroes

class TestSetMatrixZeroes(unittest.TestCase):
    def test_cases(self):
        mat = [[1,1,1],[1,0,1],[1,1,1]]
        self.assertEqual(set_zeroes(mat), [[1,0,1],[0,0,0],[1,0,1]])
        self.assertEqual(set_zeroes([[0,1],[1,1]]), [[0,0],[0,1]])
        self.assertEqual(set_zeroes([]), [])

if __name__ == "__main__":
    unittest.main()
