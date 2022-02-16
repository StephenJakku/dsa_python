class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.isEmpty() else "No elements in the Stack"

    def getStack(self):
        return self.items

    def isEmpty(self):
        return True if len(self.items)<=0 else False

# myStack=Stack()
# myStack.push(1)
# myStack.push(2)
# myStack.push(3)
# myStack.push(4)
# print(myStack.peek())
# print(myStack.getStack())
# myStack.pop()
# myStack.pop()
# print(myStack.peek())
# print(myStack.getStack())
# print(myStack.isEmpty())
# myStack.pop()
# myStack.pop()
# print(myStack.isEmpty())
# print(myStack.peek())