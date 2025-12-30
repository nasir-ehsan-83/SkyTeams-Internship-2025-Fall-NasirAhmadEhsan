import unittest
from question24 import pascal_triangle

class TestQuestion24(unittest.TestCase):
    def test_pascal_triangle(self):
        self.assertEqual(pascal_triangle(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

if __name__ == "__main__":
    unittest.main()
