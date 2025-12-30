import unittest
from question23 import fibonacci

class TestQuestion23(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), [0,1,1,2,3,5,8])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(0), [])

if __name__ == "__main__":
    unittest.main()
