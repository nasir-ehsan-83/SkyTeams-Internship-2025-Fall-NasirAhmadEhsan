import unittest
from question29 import arrays_equal

class TestQuestion29(unittest.TestCase):
    def test_arrays_equal(self):
        self.assertTrue(arrays_equal([1,2,3],[1,2,3]))
        self.assertFalse(arrays_equal([1,2,3],[1,3,2]))

if __name__ == "__main__":
    unittest.main()
