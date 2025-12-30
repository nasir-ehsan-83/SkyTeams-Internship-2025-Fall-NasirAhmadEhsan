import unittest
from question8 import Stack

class TestReverseStack(unittest.TestCase):
    def test_reverse_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.reverse()
        self.assertEqual(s.to_list(), [3,2,1])

if __name__ == "__main__":
    unittest.main()
