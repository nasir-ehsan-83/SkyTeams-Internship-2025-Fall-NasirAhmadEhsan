import unittest
from question26 import decimal_to_binary

class TestQuestion26(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(0), "0")

if __name__ == "__main__":
    unittest.main()
