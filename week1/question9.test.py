import unittest
from question9 import simple_interest, compound_interest

class TestQuestion9(unittest.TestCase):
    def test_interest(self):
        self.assertEqual(simple_interest(1000, 5, 2), 100)
        self.assertEqual(compound_interest(1000, 5, 2), 102)

if __name__ == "__main__":
    unittest.main()
