import unittest
from question27 import unique_elements

class TestQuestion27(unittest.TestCase):
    def test_unique_elements(self):
        self.assertEqual(unique_elements([1,2,2,3,4,4,5]), [1,2,3,4,5])

if __name__ == "__main__":
    unittest.main()
