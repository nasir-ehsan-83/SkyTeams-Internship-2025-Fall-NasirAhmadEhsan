class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def reverse(self):
        temp = []
        while self.items:
            temp.append(self.pop())
        self.items = temp

    def to_list(self):
        return self.items.copy()
