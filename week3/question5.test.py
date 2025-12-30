import unittest
from question5 import largest

class TestQuestion5(unittest.TestCase):
    def test_largest(self):
        self.assertEqual(largest([2,8,5,3,9]), 9)
        self.assertEqual(largest([]), None)

if __name__ == "__main__":
    unittest.main()
