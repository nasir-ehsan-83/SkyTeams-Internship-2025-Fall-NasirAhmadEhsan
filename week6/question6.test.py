import unittest
from question1 import TreeNode
from question6 import childrenSum

class TestChildrenSum(unittest.TestCase):
    def test_children_sum(self):
        root = TreeNode(10)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        self.assertTrue(childrenSum(root))

        root.right.val = 5
        self.assertFalse(childrenSum(root))

if __name__ == "__main__":
    unittest.main()
