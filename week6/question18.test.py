import unittest
from question1 import TreeNode
from question18 import bstFromPreorder

class TestBSTFromPreorder(unittest.TestCase):
    def test_bst_from_preorder(self):
        preorder = [8,5,1,7,10,12]
        root = bstFromPreorder(preorder)
        self.assertEqual(root.val, 8)
        self.assertEqual(root.left.val, 5)
        self.assertEqual(root.right.val, 10)
        self.assertEqual(root.left.left.val, 1)
        self.assertEqual(root.left.right.val, 7)
        self.assertEqual(root.right.right.val, 12)

if __name__ == "__main__":
    unittest.main()
