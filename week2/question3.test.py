import unittest
from question3 import rectangle_area_perimeter

class TestQuestion3(unittest.TestCase):
    def test_rectangle_area_perimeter(self):
        self.assertEqual(rectangle_area_perimeter(4, 6), (24, 20))
        self.assertEqual(rectangle_area_perimeter(0, 5), (0, 10))

if __name__ == "__main__":
    unittest.main()
