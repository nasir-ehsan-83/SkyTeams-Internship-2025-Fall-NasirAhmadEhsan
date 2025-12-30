import unittest
from question16 import numbers_1_to_100

class TestQuestion16(unittest.TestCase):
    def test_numbers_1_to_100(self):
        result = numbers_1_to_100()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[-1], 100)
        self.assertEqual(len(result), 100)

if __name__ == "__main__":
    unittest.main()
