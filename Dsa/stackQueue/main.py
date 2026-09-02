class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("empty stack")
            return None

        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"stack{self.items}"



class Queue:
    def __init__(self):
        self.items = []

    def Enqueue(self,item):
        self.items.append(item)

    def Dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    



stack = Stack()

stack.push(34)
stack.push(40)
stack.push(78)
stack.pop()

print(stack.is_empty())

print(stack.peek())
print(stack.__len__())
print(stack.__repr__())

