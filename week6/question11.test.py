import unittest
from question1 import TreeNode
from question11 import diameterOfTree

class TestDiameter(unittest.TestCase):
    def test_diameter(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(diameterOfTree(root), 4)

if __name__ == "__main__":
    unittest.main()
