def isBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return isBST(root.left, low, root.val) and isBST(root.right, root.val, high)
