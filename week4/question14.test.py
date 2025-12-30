import unittest
from question14 import string_permutations

class TestStringPermutations(unittest.TestCase):
    def test_cases(self):
        result = string_permutations("abc")
        expected = ['abc','acb','bac','bca','cab','cba']
        self.assertCountEqual(result, expected)
        self.assertEqual(string_permutations("a"), ['a'])
        self.assertEqual(string_permutations(""), [''])

if __name__ == "__main__":
    unittest.main()
