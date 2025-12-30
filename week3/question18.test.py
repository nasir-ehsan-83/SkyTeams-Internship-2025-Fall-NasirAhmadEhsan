import unittest
from question18 import right_aligned_triangle

class TestQuestion18(unittest.TestCase):
    def test_right_aligned_triangle(self):
        self.assertEqual(right_aligned_triangle(4), ['   *','  **',' ***','****'])

if __name__ == "__main__":
    unittest.main()
