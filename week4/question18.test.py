import unittest
from question18 import Stack

class TestStack(unittest.TestCase):
    def test_cases(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.peek(), 30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.size(), 2)
        self.assertFalse(stack.is_empty())

if __name__ == "__main__":
    unittest.main()
