import unittest
from question3 import reverse_string

class TestQuestion3(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

if __name__ == "__main__":
    unittest.main()
