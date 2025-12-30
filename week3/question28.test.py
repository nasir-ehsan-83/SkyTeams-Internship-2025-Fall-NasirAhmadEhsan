import unittest
from question28 import remove_duplicates

class TestQuestion28(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([3,1,3,5,1]), [3,1,5])

if __name__ == "__main__":
    unittest.main()
