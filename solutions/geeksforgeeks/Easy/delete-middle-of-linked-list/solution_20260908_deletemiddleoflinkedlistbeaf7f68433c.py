""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def deleteMid(self, head):
        
        if head is None or head.next is None:
            return None
            
        slow = head
        fast = head.next
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        
        return head
