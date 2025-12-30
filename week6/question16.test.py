import unittest
from question1 import TreeNode
from question16 import boundaryTraversal

class TestBoundaryTraversal(unittest.TestCase):
    def test_boundary(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.right.left = TreeNode(7)
        self.assertEqual(boundaryTraversal(root), [1,2,4,5,7,6,3])

if __name__ == "__main__":
    unittest.main()
