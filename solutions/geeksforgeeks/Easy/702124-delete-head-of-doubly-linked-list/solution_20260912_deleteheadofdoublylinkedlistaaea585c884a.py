''' Structure of doubly linked list Node
 class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteHead(self, head):
        
        if head is None or head.next is None:
            return None
            
        newHead = head.next
        head.next = None
        newHead.prev = None
        
        return newHead
