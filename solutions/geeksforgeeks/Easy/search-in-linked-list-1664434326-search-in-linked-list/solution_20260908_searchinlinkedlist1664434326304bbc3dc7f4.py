'''Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        
        current = head
        
        while current is not None:
            if current.data == key:
                return True
            
            current = current.next
            
        return False
