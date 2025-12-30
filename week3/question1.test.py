import unittest
from question1 import count_vowels

class TestQuestion1(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("SkyTeams Internship"), 6)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("bcdfg"), 0)

if __name__ == "__main__":
    unittest.main()
