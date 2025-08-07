class Queue:
    def __init__(self,capacity):
        self.queue=[0]*capacity
        self.capacity=capacity
        self.front=0
        self.rear=0

    def enqueue(self,element):
        if self.isFull():
            print("Queue Overflow")
            return
        self.queue[self.rear]=element
        self.rear+=1

    def dequeue(self):
        if self.isEmpty():
            print("Queue underflow")
            return -1
        element=self.queue[self.front]
        self.front+=1
        return element

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        element=self.queue[self.front]
        return element

    def isEmpty(self):
        if self.front==self.rear:
            return True
        return False

    def isFull(self):
        return self.rear==self.capacity

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        for i in range(self.front,self.rear):
            print(self.queue[i],end=' ')
        print()

q=Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()
q.enqueue(1)
print(q.isFull())
print(q.isEmpty())