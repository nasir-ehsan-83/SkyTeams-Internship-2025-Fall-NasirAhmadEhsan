import unittest
from question1 import TreeNode
from question19 import lowestCommonAncestor

class TestLCA(unittest.TestCase):
    def test_lca(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        p = root.left
        q = root.right
        self.assertEqual(lowestCommonAncestor(root, p, q).val, 3)

if __name__ == "__main__":
    unittest.main()
