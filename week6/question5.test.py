import unittest
from question1 import TreeNode
from question5 import isBalanced

class TestBalancedTree(unittest.TestCase):
    def test_balanced(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertTrue(isBalanced(root))

        root.left.left.left = TreeNode(6)
        self.assertFalse(isBalanced(root))

if __name__ == "__main__":
    unittest.main()
