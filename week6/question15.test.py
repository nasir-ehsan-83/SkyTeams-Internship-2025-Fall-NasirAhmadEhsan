import unittest
from question1 import TreeNode
from question15 import zigzagLevelOrder

class TestZigzagTraversal(unittest.TestCase):
    def test_zigzag(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(zigzagLevelOrder(root), [[1],[3,2],[4,5]])

if __name__ == "__main__":
    unittest.main()
