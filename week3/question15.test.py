import unittest
from question15 import is_armstrong

class TestQuestion15(unittest.TestCase):
    def test_is_armstrong(self):
        self.assertTrue(is_armstrong(153))
        self.assertFalse(is_armstrong(123))

if __name__ == "__main__":
    unittest.main()
