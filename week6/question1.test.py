import unittest
from question1 import TreeNode, treeHeight

class TestTreeHeight(unittest.TestCase):
    def test_height(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(treeHeight(root), 3)
        self.assertEqual(treeHeight(None), 0)

if __name__ == "__main__":
    unittest.main()
