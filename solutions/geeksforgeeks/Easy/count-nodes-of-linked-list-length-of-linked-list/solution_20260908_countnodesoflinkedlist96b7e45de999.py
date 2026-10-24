''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        
        length = 0
        
        current = head
        
        while current is not None:
            current = current.next
            length += 1
            
        return length
