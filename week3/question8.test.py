import unittest
from question8 import contains

class TestQuestion8(unittest.TestCase):
    def test_contains(self):
        self.assertTrue(contains([3,6,9,12], 6))
        self.assertFalse(contains([3,6,9,12], 7))

if __name__ == "__main__":
    unittest.main()
