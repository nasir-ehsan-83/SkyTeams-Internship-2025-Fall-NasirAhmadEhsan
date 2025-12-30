from week6.question1 import TreeNode


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    index = inorder.index(root_val)
    root.left = buildTree(preorder[1:index+1], inorder[:index])
    root.right = buildTree(preorder[index+1:], inorder[index+1:])
    return root
