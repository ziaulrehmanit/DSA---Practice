class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class myQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0
        
    def enqueue(self, x):
        newNode = Node(x)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next= newNode
            self.tail = newNode
            
        self.length += 1
        
    def dequeue(self):
        if self.head is None:
            return -1
            
        temp = self.head.data
        self.head = self.head.next
        self.length -= 1
        
        if self.length == 0:
            self.tail = None
            
        return temp

    def getFront(self):
        return -1 if self.length == 0 else self.head.data

    def size(self):
        return self.length
