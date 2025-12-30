import unittest
from question1 import TreeNode
from question17 import buildTree

class TestBuildTree(unittest.TestCase):
    def test_build_tree(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        root = buildTree(preorder, inorder)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)

if __name__ == "__main__":
    unittest.main()
