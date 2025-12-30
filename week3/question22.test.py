import unittest
from question22 import collatz_sequence

class TestQuestion22(unittest.TestCase):
    def test_collatz_sequence(self):
        self.assertEqual(collatz_sequence(6), ([6,3,10,5,16,8,4,2,1], 8))

if __name__ == "__main__":
    unittest.main()
