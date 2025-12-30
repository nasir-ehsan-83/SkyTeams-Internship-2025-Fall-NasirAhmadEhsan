import unittest
from question17 import right_triangle

class TestQuestion17(unittest.TestCase):
    def test_right_triangle(self):
        self.assertEqual(right_triangle(4), ['*','**','***','****'])

if __name__ == "__main__":
    unittest.main()
