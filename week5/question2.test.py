import unittest
from question2 import SinglyLinkedListWithInsert

class TestInsertAtBeginning(unittest.TestCase):
    def test_insert_beginning(self):
        sll = SinglyLinkedListWithInsert()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        sll.insert_at_beginning(5)
        self.assertEqual(sll.to_list(), [5, 10, 20, 30])