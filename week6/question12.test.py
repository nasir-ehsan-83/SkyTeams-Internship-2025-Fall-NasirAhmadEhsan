import unittest
from question1 import TreeNode
from question12 import isSubtree

class TestIsSubtree(unittest.TestCase):
    def test_subtree(self):
        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)

        self.assertTrue(isSubtree(s, t))

if __name__ == "__main__":
    unittest.main()
