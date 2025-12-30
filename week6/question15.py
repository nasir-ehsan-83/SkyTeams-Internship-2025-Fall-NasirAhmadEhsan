def zigzagLevelOrder(root):
    if not root:
        return []
    result, level, stack = [], [root], 0
    while level:
        current = []
        next_level = []
        for node in level:
            current.append(node.val)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        if stack % 2 == 1:
            current.reverse()
        result.append(current)
        level = next_level
        stack += 1
    return result
