import unittest
from question1 import TreeNode
from question14 import countSingleValuedSubtrees

class TestSingleValuedSubtrees(unittest.TestCase):
    def test_count_single_valued(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        root.right.left = TreeNode(5)
        self.assertEqual(countSingleValuedSubtrees(root), 4)

if __name__ == "__main__":
    unittest.main()
