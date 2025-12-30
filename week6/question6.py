def childrenSum(root):
    if not root or (not root.left and not root.right):
        return True
    left_val = root.left.val if root.left else 0
    right_val = root.right.val if root.right else 0
    return (root.val == left_val + right_val) and childrenSum(root.left) and childrenSum(root.right)
