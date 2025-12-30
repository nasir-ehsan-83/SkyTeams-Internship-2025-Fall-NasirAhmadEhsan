import unittest
from question20 import count_digits

class TestQuestion20(unittest.TestCase):
    def test_count_digits(self):
        self.assertEqual(count_digits(786), 3)
        self.assertEqual(count_digits(0), 0)

if __name__ == "__main__":
    unittest.main()
