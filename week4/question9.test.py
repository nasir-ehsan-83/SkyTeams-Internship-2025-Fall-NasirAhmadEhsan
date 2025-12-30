import unittest
from question9 import compress_string

class TestCompressString(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("abc"), "a1b1c1")

if __name__ == "__main__":
    unittest.main()
