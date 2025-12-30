import unittest
from question1 import TreeNode
from question13 import isBST

class TestIsBST(unittest.TestCase):
    def test_is_bst(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(isBST(root))
        root.right.val = 0
        self.assertFalse(isBST(root))

if __name__ == "__main__":
    unittest.main()
