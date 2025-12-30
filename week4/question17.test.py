import unittest
from question17 import abbreviate_sentence

class TestAbbreviateSentence(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(abbreviate_sentence("I am learning JavaScript"), "I a l J")
        self.assertEqual(abbreviate_sentence("Hello World"), "H W")
        self.assertEqual(abbreviate_sentence(""), "")

if __name__ == "__main__":
    unittest.main()
