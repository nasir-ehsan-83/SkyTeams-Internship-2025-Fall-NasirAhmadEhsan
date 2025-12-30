import unittest
from question21 import sum_of_digits

class TestQuestion21(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(786), 21)

if __name__ == "__main__":
    unittest.main()
