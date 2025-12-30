import unittest
from question9 import grade

class TestQuestion9(unittest.TestCase):
    def test_grade(self):
        self.assertEqual(grade(95), "A")
        self.assertEqual(grade(85), "B")
        self.assertEqual(grade(50), "F")

if __name__ == "__main__":
    unittest.main()
