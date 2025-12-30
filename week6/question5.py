def isBalanced(root):
    def helper(node):
        if not node:
            return 0, True
        left_height, left_balanced = helper(node.left)
        right_height, right_balanced = helper(node.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, balanced
    return helper(root)[1]
