class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)

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

    def clear(self):
        self.items.clear()




class BrowserHistory:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()

    def visit(self, site):
        self.back_stack.push(site)
        self.forward_stack.clear()

    def back(self):
        if len(self.back_stack) <= 1:
            print("no history recorded")
            return 
        site = self.back_stack.pop()
        self.forward_stack.push(site)
    
        return site

    def current_page(self):
        return self.back_stack.peek()
    

    def forword(self):

        site = self.forward_stack.peek()

    def forward(self):
        if self.forward_stack.is_empty():
            return None
            
        site = self.forward_stack.peek()
        self.back_stack.push(site)

        self.forward_stack.clear()
        return site

history = BrowserHistory()

history.visit("Google")
history.visit("YouTube")
history.visit("GitHub")

print(history.back())

print(history.forword())

print(history.forward())

print(history.current_page())
history.visit("GitHub")

