import unittest
from question22 import even_numbers

class TestQuestion22(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(even_numbers(1,10), [2,4,6,8,10])
        self.assertEqual(even_numbers(3,7), [4,6])

if __name__ == "__main__":
    unittest.main()
