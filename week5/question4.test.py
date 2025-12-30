import unittest
from question4 import SinglyLinkedList

class TestDeleteFirstNode(unittest.TestCase):
    def test_delete_first(self):
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.delete_first()
        self.assertEqual(ll.to_list(), [20,30])

if __name__ == "__main__":
    unittest.main()
