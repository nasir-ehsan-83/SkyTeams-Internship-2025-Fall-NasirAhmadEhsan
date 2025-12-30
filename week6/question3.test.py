import unittest
from question1 import TreeNode
from question3 import mirrorTree

class TestMirrorTree(unittest.TestCase):
    def test_mirror(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        mirrored = mirrorTree(root)
        self.assertEqual(mirrored.left.val, 3)
        self.assertEqual(mirrored.right.val, 2)

if __name__ == "__main__":
    unittest.main()
