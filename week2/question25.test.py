import unittest
from question25 import lcm

class TestQuestion25(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(12,18), 36)
        self.assertEqual(lcm(7,5), 35)

if __name__ == "__main__":
    unittest.main()
