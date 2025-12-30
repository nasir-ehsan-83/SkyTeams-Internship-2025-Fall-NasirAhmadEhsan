def nodesAtDistanceK(root, k):
    result = []
    def dfs(node, level):
        if not node:
            return
        if level == k:
            result.append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    dfs(root, 0)
    return result
