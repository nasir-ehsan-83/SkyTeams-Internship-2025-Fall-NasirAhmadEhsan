def printAncestors(root, target):
    result = []
    def helper(node):
        if not node:
            return False
        if node.val == target or helper(node.left) or helper(node.right):
            if node.val != target:
                result.append(node.val)
            return True
        return False
    helper(root)
    return result
