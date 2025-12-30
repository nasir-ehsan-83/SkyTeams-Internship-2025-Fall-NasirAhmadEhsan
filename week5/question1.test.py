import unittest
from question1 import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_linked_list_creation(self):
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(ll.to_list(), [10,20,30])

if __name__ == "__main__":
    unittest.main()
