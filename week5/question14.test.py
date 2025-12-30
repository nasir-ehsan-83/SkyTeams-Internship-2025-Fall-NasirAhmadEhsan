import unittest
from question14 import removeAdjacent

class TestRemoveAdjacent(unittest.TestCase):
    def test_remove_adjacent(self):
        self.assertEqual(removeAdjacent("abbaca"), "ca")
        self.assertEqual(removeAdjacent("aabbcc"), "")
        self.assertEqual(removeAdjacent("abc"), "abc")

if __name__ == "__main__":
    unittest.main()
