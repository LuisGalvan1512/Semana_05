class QueueWithStacks:
    def __init__(self):
        self.in_stack = []  
        self.out_stack = []  

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def size(self):
        return len(self.in_stack) + len(self.out_stack)


# Tests  

q = QueueWithStacks()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.peek())       # Expected output: "A"
print(q.dequeue())    # Expected output: "A"
print(q.peek())       # Expected output: "B"
print(q.size())       # Expected output: 2
print(q.is_empty())   # Expected output: False

q.dequeue()
q.dequeue()
print(q.is_empty())   # Expected output: True

# Uncommenting the following line should raise an error
# q.dequeue()  # IndexError: Queue is empty! 🚫
