def countSingleValuedSubtrees(root):
    count = [0]
    def helper(node):
        if not node:
            return True
        left = helper(node.left)
        right = helper(node.right)
        if left and right:
            if (node.left and node.left.val != node.val) or (node.right and node.right.val != node.val):
                return False
            count[0] += 1
            return True
        return False
    helper(root)
    return count[0]
