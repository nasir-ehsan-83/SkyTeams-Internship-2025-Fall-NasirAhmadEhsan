def boundaryTraversal(root):
    if not root:
        return []
    res = [root.val]

    def leftBoundary(node):
        temp = []
        while node:
            if node.left or node.right:
                temp.append(node.val)
            node = node.left if node.left else node.right
        return temp

    def rightBoundary(node):
        temp = []
        while node:
            if node.left or node.right:
                temp.append(node.val)
            node = node.right if node.right else node.left
        return temp[::-1]

    def leaves(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return leaves(node.left) + leaves(node.right)

    if root.left:
        res += leftBoundary(root.left)
    res += leaves(root.left) + leaves(root.right)
    if root.right:
        res += rightBoundary(root.right)
    return res
