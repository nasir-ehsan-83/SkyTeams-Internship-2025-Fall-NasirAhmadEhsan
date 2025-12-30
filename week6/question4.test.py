import unittest
from question1 import TreeNode
from question4 import isSymmetric

class TestSymmetricTree(unittest.TestCase):
    def test_symmetric(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(isSymmetric(root))

        root.right.right.val = 5
        self.assertFalse(isSymmetric(root))

if __name__ == "__main__":
    unittest.main()
