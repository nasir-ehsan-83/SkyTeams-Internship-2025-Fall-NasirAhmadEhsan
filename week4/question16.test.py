import unittest
from question16 import multiply_matrix

class TestMultiplyMatrix(unittest.TestCase):
    def test_cases(self):
        A = [[1,2],[3,4]]
        B = [[5,6],[7,8]]
        self.assertEqual(multiply_matrix(A,B), [[19,22],[43,50]])
        self.assertEqual(multiply_matrix([[1]], [[2]]), [[2]])
        self.assertIsNone(multiply_matrix([[1,2]], [[1,2]]))

if __name__ == "__main__":
    unittest.main()
