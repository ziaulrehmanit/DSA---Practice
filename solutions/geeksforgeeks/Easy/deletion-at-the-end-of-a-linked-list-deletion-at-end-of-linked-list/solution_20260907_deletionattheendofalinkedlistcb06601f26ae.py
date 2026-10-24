'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def removeLastNode(self, head):
        
        if head is None or head.next is None:
            return None
            
        current = head
        while current.next.next is not None:
            current = current.next
        
        current.next = None
        
        return head
