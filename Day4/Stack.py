class Stack:
    def __init__(self, capacity):
        self.stack = [0] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, item):
        if self.isFull():
            print("Stack overflow")
            return
        self.top += 1
        self.stack[self.top] = item


    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return -1
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Stack underflow")
            return -1
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def isFull(self):
        return self.top == self.capacity - 1

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.top+1):
                print(self.stack[i])

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top element:", s.peek())
s.pop()
s.display()
print("Stack is empty?", s.is_empty())
print("Stack size:", s.size())
s.pop()
s.display()
print("Stack is full?", s.isFull())
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.display()
print("Stack is full?", s.isFull())