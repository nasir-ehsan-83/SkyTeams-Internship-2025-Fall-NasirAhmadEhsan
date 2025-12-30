import unittest
from question1 import TreeNode
from question20 import printAncestors

class TestAncestors(unittest.TestCase):
    def test_ancestors(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(printAncestors(root, 5), [2,1])

if __name__ == "__main__":
    unittest.main()
