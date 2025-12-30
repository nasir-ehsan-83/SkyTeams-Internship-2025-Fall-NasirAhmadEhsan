import unittest
from question1 import TreeNode
from question9 import inorderSuccessor

class TestInorderSuccessor(unittest.TestCase):
    def test_successor(self):
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(15)
        node = root.left
        self.assertEqual(inorderSuccessor(root, node).val, 15)

if __name__ == "__main__":
    unittest.main()
