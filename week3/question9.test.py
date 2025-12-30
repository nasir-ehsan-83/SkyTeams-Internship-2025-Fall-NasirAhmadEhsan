import unittest
from question9 import count_occurrences

class TestQuestion9(unittest.TestCase):
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([2,3,2,5,2], 2), 3)
        self.assertEqual(count_occurrences([1,2,3], 4), 0)

if __name__ == "__main__":
    unittest.main()
