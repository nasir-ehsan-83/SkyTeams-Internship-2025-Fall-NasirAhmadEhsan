from week6.question1 import TreeNode


def bstFromPreorder(preorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    for val in preorder[1:]:
        insertBST(root, val)
    return root

def insertBST(node, val):
    if val < node.val:
        if node.left:
            insertBST(node.left, val)
        else:
            node.left = TreeNode(val)
    else:
        if node.right:
            insertBST(node.right, val)
        else:
            node.right = TreeNode(val)
