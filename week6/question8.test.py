import unittest
from question1 import TreeNode
from question8 import nodesAtDistanceK

class TestNodesAtDistanceK(unittest.TestCase):
    def test_nodes_distance_k(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(nodesAtDistanceK(root, 2), [4,5])

if __name__ == "__main__":
    unittest.main()
