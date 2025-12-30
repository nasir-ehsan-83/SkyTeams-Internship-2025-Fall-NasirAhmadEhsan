import unittest
from question6 import seconds_to_hms

class TestQuestion6(unittest.TestCase):
    def test_seconds_to_hms(self):
        self.assertEqual(seconds_to_hms(3665), (1, 1, 5))
        self.assertEqual(seconds_to_hms(59), (0, 0, 59))

if __name__ == "__main__":
    unittest.main()
