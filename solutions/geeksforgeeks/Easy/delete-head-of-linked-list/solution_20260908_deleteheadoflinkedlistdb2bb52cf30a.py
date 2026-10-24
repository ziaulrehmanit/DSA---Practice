'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteHead(self, head):
        
        if head is None or head.next is None:
            return None
            
        head = head.next
        
        return head
