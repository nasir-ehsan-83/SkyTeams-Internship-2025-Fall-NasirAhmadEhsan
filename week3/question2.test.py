import unittest
from question2 import reverse_number

class TestQuestion2(unittest.TestCase):
    def test_reverse_number(self):
        self.assertEqual(reverse_number(1234), 4321)
        self.assertEqual(reverse_number(100), 1)
        self.assertEqual(reverse_number(0), 0)

if __name__ == "__main__":
    unittest.main()
