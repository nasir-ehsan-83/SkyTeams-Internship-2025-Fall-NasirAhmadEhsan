import unittest
from question11 import is_rotation

class TestIsRotation(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_rotation("waterbottle","erbottlewat"))
        self.assertFalse(is_rotation("abc","acb"))
        self.assertTrue(is_rotation("",""))

if __name__ == "__main__":
    unittest.main()
