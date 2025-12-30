import unittest
from question8 import number_type

class TestQuestion8(unittest.TestCase):
    def test_number_type(self):
        self.assertEqual(number_type(5), "Positive")
        self.assertEqual(number_type(-3), "Negative")
        self.assertEqual(number_type(0), "Zero")

if __name__ == "__main__":
    unittest.main()
