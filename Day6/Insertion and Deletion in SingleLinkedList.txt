class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_pos(self, val, pos):
        n = Node(val)
        if pos == 1:
            n.next = self.head
            self.head = n
            return
        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next
        n.next = temp.next
        temp.next = n

    def delete_at_pos(self, pos):
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next

ll = LinkedList()
ll.insert_at_pos(10, 1)
ll.insert_at_pos(20, 2)
ll.insert_at_pos(15, 2)
ll.display()
ll.delete_at_pos(2)
ll.display()