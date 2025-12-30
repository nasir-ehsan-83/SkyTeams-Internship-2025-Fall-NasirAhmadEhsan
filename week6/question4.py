def isSymmetric(root):
    def check(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and check(t1.left, t2.right) and check(t1.right, t2.left)
    return check(root.left, root.right) if root else True
