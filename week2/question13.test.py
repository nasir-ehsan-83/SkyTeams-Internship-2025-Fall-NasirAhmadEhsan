import unittest
from question13 import month_info

class TestQuestion13(unittest.TestCase):
    def test_month_info(self):
        self.assertEqual(month_info(2), ("February", 28))
        self.assertEqual(month_info(4), ("April", 30))
        self.assertEqual(month_info(13), ("Invalid", 0))

if __name__ == "__main__":
    unittest.main()
