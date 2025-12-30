import unittest
from question1 import TreeNode
from question7 import sortedArrayToBST

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

class TestArrayToBST(unittest.TestCase):
    def test_array_to_bst(self):
        arr = [1,2,3,4,5]
        root = sortedArrayToBST(arr)
        self.assertEqual(inorder(root), arr)

if __name__ == "__main__":
    unittest.main()
