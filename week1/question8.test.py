import unittest
from question8 import c_to_f, f_to_c

class TestQuestion8(unittest.TestCase):
    def test_c_to_f(self):
        self.assertEqual(c_to_f(25), 77)
    def test_f_to_c(self):
        self.assertEqual(f_to_c(77), 25)

if __name__ == "__main__":
    unittest.main()
