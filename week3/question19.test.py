import unittest
from question19 import pyramid

class TestQuestion19(unittest.TestCase):
    def test_pyramid(self):
        self.assertEqual(pyramid(5), ['    *','   ***','  *****',' *******','*********'])

if __name__ == "__main__":
    unittest.main()
