''' Structure of linked list Node
 class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 
'''

class myStack:

    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def push(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def pop(self):
        if self.head is None:
            return -1
        temp = self.head.data
        self.head = self.head.next
        self.length -= 1
        return temp


    def peek(self):
        if self.head is None:
            return -1
        return self.head.data


    def size(self):
        return self.length
