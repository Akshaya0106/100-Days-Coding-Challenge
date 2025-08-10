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

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print()

    def display_reverse(self, node):
        if node is None:
            return
        self.display_reverse(node.next)
        print(node.val, end=" -> ")

ll = LinkedList()
ll.insert_at_pos(10, 1)
ll.insert_at_pos(20, 2)
ll.insert_at_pos(15, 2)

print("Normal order:")
ll.display()

print("Reverse order:")
ll.display_reverse(ll.head)


