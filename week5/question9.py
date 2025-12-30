def isValid(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()
    return not stack
