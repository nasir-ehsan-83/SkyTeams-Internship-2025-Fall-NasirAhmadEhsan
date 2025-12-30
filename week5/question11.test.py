import unittest
from question11 import QueueTwoStacks

class TestQueueTwoStacks(unittest.TestCase):
    def test_queue_two_stacks(self):
        q = QueueTwoStacks()
        self.assertTrue(q.empty())
        q.push(10)
        q.push(20)
        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.peek(), 20)

if __name__ == "__main__":
    unittest.main()
