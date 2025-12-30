def kthLargest(root, k):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.right
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.left
