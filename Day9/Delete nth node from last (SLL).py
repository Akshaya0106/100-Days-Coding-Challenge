class Node:
    def __init__(self, val):  # fixed __init__ spelling
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):  # fixed __init__ spelling
        self.root = None

    def addNewNode(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    def delete_nth_from_last(self, n):
        dummy = Node(0)
        dummy.next = self.root
        fast = dummy
        slow = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            if fast is None:
                print("List has fewer nodes than given position")
                return
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Delete the node
        if slow.next is not None:
            slow.next = slow.next.next
        self.root = dummy.next

    def display(self):
        temp = self.root
        while temp is not None:
            print(temp.val, "->", end='')
            temp = temp.next
        print('SLL is empty')


# Example usage
s = SingleLinkedList()
s.addNewNode(10)
s.addNewNode(20)
s.addNewNode(30)
s.addNewNode(40)
s.addNewNode(50)

print("Original list:")
s.display()

s.delete_nth_from_last(2)
print("After deleting 2nd node from last:")
s.display()