import unittest
from question6 import min_of_three

class TestQuestion6(unittest.TestCase):
    def test_min_of_three(self):
        self.assertEqual(min_of_three(3, 9, 5), 3)
        self.assertEqual(min_of_three(0, -1, -2), -2)

if __name__ == "__main__":
    unittest.main()
