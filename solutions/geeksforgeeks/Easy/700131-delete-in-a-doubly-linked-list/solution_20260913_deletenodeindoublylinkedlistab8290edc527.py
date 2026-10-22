""" Structure of a Doubly Linked List Node
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        
        if head is None:
            return None
        
        if x == 1:
            newHead = head.next
            if newHead:
                newHead.prev = None
                return newHead
            return None
            
        curr = head    
        ind = 1
        while ind < x:
            if curr is None:
                return head
            curr = curr.next
            ind += 1
        
        if curr is None:
            return head
            
        if curr.next is None:
            curr.prev.next = None
            return head
            
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        
        return head
