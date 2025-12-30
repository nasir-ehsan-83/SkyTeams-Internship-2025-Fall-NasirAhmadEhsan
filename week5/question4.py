class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        from question1 import Node
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
