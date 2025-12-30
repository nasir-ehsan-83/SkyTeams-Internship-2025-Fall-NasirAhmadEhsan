import unittest
from question7 import rectangle_area_perimeter

class TestQuestion7(unittest.TestCase):
    def test_rectangle_area_perimeter(self):
        area, perimeter = rectangle_area_perimeter(4, 6)
        self.assertEqual((area, perimeter), (24, 20))
        area, perimeter = rectangle_area_perimeter(0, 5)
        self.assertEqual((area, perimeter), (0, 10))

if __name__ == "__main__":
    unittest.main()
