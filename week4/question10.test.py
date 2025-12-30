import unittest
from question10 import is_unique

class TestIsUnique(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_unique("abc"))
        self.assertFalse(is_unique("hello"))
        self.assertTrue(is_unique(""))

if __name__ == "__main__":
    unittest.main()
