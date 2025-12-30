def isSubtree(s, t):
    def isSame(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and isSame(a.left, b.left) and isSame(a.right, b.right)
    if not s:
        return False
    if isSame(s, t):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)
