import unittest
from question5 import max_of_three

class TestQuestion5(unittest.TestCase):
    def test_max_of_three(self):
        self.assertEqual(max_of_three(3, 9, 5), 9)
        self.assertEqual(max_of_three(0, -1, -2), 0)

if __name__ == "__main__":
    unittest.main()
