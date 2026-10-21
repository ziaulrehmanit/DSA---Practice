'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        
        if head.next is None:
            return head
            
        slow = head
        fast = head.next
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        slow = slow.next
        
        return slow.data
