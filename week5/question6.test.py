import unittest
from question6 import Queue

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        q = Queue()
        self.assertTrue(q.isEmpty())
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        self.assertEqual(q.to_list(), [10,20,30])
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.to_list(), [20,30])
        self.assertEqual(q.front(), 20)
        self.assertEqual(q.rear(), 30)

if __name__ == "__main__":
    unittest.main()
