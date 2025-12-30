import unittest
from question1 import second_largest

class TestSecondLargest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(second_largest([10, 20, 4, 45, 99]), 45)
        self.assertEqual(second_largest([1,2]), 1)
        self.assertEqual(second_largest([5,5,5]), None)
        self.assertEqual(second_largest([1]), None)

if __name__ == "__main__":
    unittest.main()
