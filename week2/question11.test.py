import unittest
from question11 import calculator

class TestQuestion11(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(calculator(5, 3, '+'), 8)
        self.assertEqual(calculator(5, 3, '-'), 2)
        self.assertEqual(calculator(5, 3, '*'), 15)
        self.assertEqual(calculator(6, 3, '/'), 2)
        self.assertIsNone(calculator(6, 0, '/'))

if __name__ == "__main__":
    unittest.main()
