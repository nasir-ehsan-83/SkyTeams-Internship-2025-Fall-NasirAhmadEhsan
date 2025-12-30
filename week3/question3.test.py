import unittest
from question3 import sum_of_digits

class TestQuestion3(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(0), 0)

if __name__ == "__main__":
    unittest.main()
