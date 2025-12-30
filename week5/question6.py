class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def isEmpty(self):
        return self.front_node is None

    def enqueue(self, val):
        new_node = Node(val)
        if self.rear_node:
            self.rear_node.next = new_node
        self.rear_node = new_node
        if not self.front_node:
            self.front_node = new_node

    def dequeue(self):
        if self.isEmpty():
            return None
        removed = self.front_node.val
        self.front_node = self.front_node.next
        if not self.front_node:
            self.rear_node = None
        return removed

    def front(self):
        if self.isEmpty():
            return None
        return self.front_node.val

    def rear(self):
        if self.isEmpty():
            return None
        return self.rear_node.val

    def to_list(self):
        result = []
        curr = self.front_node
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
