import unittest
from question10 import MinStack

class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        s = MinStack()
        s.push(5)
        s.push(3)
        s.push(7)
        self.assertEqual(s.getMin(), 3)
        s.pop()
        self.assertEqual(s.getMin(), 3)
        s.pop()
        self.assertEqual(s.getMin(), 5)

if __name__ == "__main__":
    unittest.main()
