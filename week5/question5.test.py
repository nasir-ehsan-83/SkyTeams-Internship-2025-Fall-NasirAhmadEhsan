import unittest
from question5 import SinglyLinkedList

class TestSearchLinkedList(unittest.TestCase):
    def test_search(self):
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        self.assertTrue(ll.search(20))
        self.assertFalse(ll.search(30))

if __name__ == "__main__":
    unittest.main()
