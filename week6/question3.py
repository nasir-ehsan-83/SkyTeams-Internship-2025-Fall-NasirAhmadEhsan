def mirrorTree(root):
    if not root:
        return None
    root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
    return root
