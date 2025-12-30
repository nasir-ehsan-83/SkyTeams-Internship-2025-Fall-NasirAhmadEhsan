import unittest
from question4 import intersection

class TestIntersection(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(intersection([1,2,3,4],[3,4,5,6]), [3,4])
        self.assertEqual(intersection([1,1,2],[1,2]), [1,2])
        self.assertEqual(intersection([], [1,2]), [])
        self.assertEqual(intersection([1,2], []), [])

if __name__ == "__main__":
    unittest.main()
