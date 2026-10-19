"""
structure of link list node
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""    
class Solution:
    def isEven(self, head):
        
        length = 0
        
        current = head
        
        while current:
            length += 1
            current = current.next
            
        return not (length % 2)
