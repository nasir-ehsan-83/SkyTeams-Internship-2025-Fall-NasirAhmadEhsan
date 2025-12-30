import unittest
from question30 import find_missing_number

class TestQuestion30(unittest.TestCase):
    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([1,2,4,5],5),3)
        self.assertEqual(find_missing_number([1,2,3,4,5],5),0)

if __name__ == "__main__":
    unittest.main()
