import unittest
from question19 import reverse_number

class TestQuestion19(unittest.TestCase):
    def test_reverse_number(self):
        self.assertEqual(reverse_number(1234), 4321)
        self.assertEqual(reverse_number(100), 1)

if __name__ == "__main__":
    unittest.main()
