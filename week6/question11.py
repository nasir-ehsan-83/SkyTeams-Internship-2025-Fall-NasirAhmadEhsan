def diameterOfTree(root):
    diameter = [0]
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter[0] = max(diameter[0], left + right + 1)
        return max(left, right) + 1
    height(root)
    return diameter[0]
