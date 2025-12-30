def isIdentical(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.val == t2.val and isIdentical(t1.left, t2.left) and isIdentical(t1.right, t2.right)
