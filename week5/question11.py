class QueueTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, val):
        self.stack_in.append(val)

    def pop(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            return None
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            return None
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out
