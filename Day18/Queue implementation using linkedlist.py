class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:   # Empty queue
            self.front = self.rear = new_node
            print(f"Enqueued: {data}")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Nothing to dequeue.")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued: {temp.data}")
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        temp = self.front
        print("Queue elements:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
print("Front element:", q.peek())
