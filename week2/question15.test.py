import unittest
from question15 import triangle_type

class TestQuestion15(unittest.TestCase):
    def test_triangle_type(self):
        self.assertEqual(triangle_type(3,3,3), "Equilateral")
        self.assertEqual(triangle_type(3,3,5), "Isosceles")
        self.assertEqual(triangle_type(3,4,5), "Scalene")
        self.assertEqual(triangle_type(1,2,3), "Invalid")

if __name__ == "__main__":
    unittest.main()
