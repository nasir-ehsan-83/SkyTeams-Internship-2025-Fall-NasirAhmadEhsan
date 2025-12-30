import unittest
from question7 import Stack

class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack()
        self.assertTrue(s.isEmpty())
        s.push(10)
        s.push(20)
        s.push(30)
        self.assertEqual(s.to_list(), [10,20,30])
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.top(), 20)
        self.assertFalse(s.isEmpty())
        self.assertEqual(s.size(), 2)

if __name__ == "__main__":
    unittest.main()
