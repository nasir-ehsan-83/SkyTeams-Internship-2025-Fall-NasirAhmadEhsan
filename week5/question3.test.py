import unittest
from question3 import SinglyLinkedList 

class TestSinglyLinkedList(unittest.TestCase):
    def test_append(self):
        sll = SinglyLinkedList()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        self.assertEqual(sll.to_list(), [10, 20, 30])
        
        # Test appending to an existing list
        sll.append(40)
        self.assertEqual(sll.to_list(), [10, 20, 30, 40])

if __name__ == "__main__":
    unittest.main()
