class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.isEmpty==0:
            return self.items.pop()
    def peek(self):
        if not self.isEmpty==0:
            return self.items[-1]
    def isEmpty(self):
        return len(self.items)==0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

