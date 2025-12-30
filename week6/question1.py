class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def treeHeight(root):
    if not root:
        return 0
    left = treeHeight(root.left)
    right = treeHeight(root.right)
    return max(left, right) + 1
