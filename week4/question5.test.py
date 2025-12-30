import unittest
from question5 import rearrange_even_odd

class TestRearrangeEvenOdd(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(rearrange_even_odd([1,2,3,4,5,6]), [2,4,6,1,3,5])
        self.assertEqual(rearrange_even_odd([2,4,6]), [2,4,6])
        self.assertEqual(rearrange_even_odd([1,3,5]), [1,3,5])
        self.assertEqual(rearrange_even_odd([]), [])

if __name__ == "__main__":
    unittest.main()
