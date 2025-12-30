import unittest
from question6 import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(binary_search([1,3,5,7,9], 7), 3)
        self.assertEqual(binary_search([1,3,5,7,9], 2), -1)
        self.assertEqual(binary_search([], 1), -1)
        self.assertEqual(binary_search([1], 1), 0)

if __name__ == "__main__":
    unittest.main()
