import unittest
from question1 import TreeNode
from question2 import isIdentical

class TestIdenticalTrees(unittest.TestCase):
    def test_identical(self):
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)

        t2 = TreeNode(1)
        t2.left = TreeNode(2)
        t2.right = TreeNode(3)

        t3 = TreeNode(1)
        t3.left = TreeNode(2)

        self.assertTrue(isIdentical(t1, t2))
        self.assertFalse(isIdentical(t1, t3))

if __name__ == "__main__":
    unittest.main()
