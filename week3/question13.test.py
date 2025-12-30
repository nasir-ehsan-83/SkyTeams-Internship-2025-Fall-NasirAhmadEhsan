import unittest
from question13 import power

class TestQuestion13(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2,5), 32)
        self.assertEqual(power(3,0), 1)

if __name__ == "__main__":
    unittest.main()
