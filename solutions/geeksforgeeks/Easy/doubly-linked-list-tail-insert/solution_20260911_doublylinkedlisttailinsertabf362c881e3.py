''' Structure of doubly linked list node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None
'''
class Solution:
    def insertInTail(self, head, value):
        
        newNode = Node(value)
        
        if head is None:
            return newNode
            
        n = 0
        curr = head
        
        while curr.next is not None:
            curr = curr.next
            
        curr.next = newNode
        newNode.prev = curr
        
        return head
