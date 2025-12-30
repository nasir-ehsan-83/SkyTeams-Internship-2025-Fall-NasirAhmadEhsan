import unittest
from question19 import QueueUsingStacks

class TestQueueUsingStacks(unittest.TestCase):
    def test_cases(self):
        q = QueueUsingStacks()
        self.assertTrue(q.empty())
        q.push(10)
        q.push(20)
        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.pop(), 20)
        self.assertTrue(q.empty())

if __name__ == "__main__":
    unittest.main()
