'''  
@author: 22000409 Kaushal Ramoliya  
@description: 2. - Write a python program to implement stack and queue using OOP paradigm.
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue


if __name__ == "__main__":
    print("Testing Stack:")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushing 10, 20, 30:", stack.display())
    print("Popped element:", stack.pop())
    print("Stack after popping:", stack.display())
    print("Is stack empty?", stack.is_empty())

    print("\nTesting Queue:")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueuing 10, 20, 30:", queue.display())
    if not queue.is_empty():
        removed_element = queue.queue.pop(0)  # Manual removal of the first element
        print("Dequeued element:", removed_element)
    else:
        print("Queue is empty")
    print("Queue after dequeuing:", queue.display())
    print("Is queue empty?", queue.is_empty())