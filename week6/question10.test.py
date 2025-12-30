import unittest
from question1 import TreeNode
from question10 import kthLargest

class TestKthLargest(unittest.TestCase):
    def test_kth_largest(self):
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(15)
        self.assertEqual(kthLargest(root, 1), 30)
        self.assertEqual(kthLargest(root, 3), 15)

if __name__ == "__main__":
    unittest.main()
