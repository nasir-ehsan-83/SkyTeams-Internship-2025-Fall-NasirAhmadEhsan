import unittest
from question3 import rotate_right

class TestRotateRight(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(rotate_right([1,2,3,4,5], 2), [4,5,1,2,3])
        self.assertEqual(rotate_right([1,2,3], 3), [1,2,3])
        self.assertEqual(rotate_right([], 5), [])
        self.assertEqual(rotate_right([1], 10), [1])

if __name__ == "__main__":
    unittest.main()
