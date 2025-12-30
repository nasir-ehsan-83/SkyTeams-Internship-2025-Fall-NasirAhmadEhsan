def backspaceCompare(s, t):
    def process(string):
        stack = []
        for c in string:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
    return process(s) == process(t)
