"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteKthElement(self, head: ListNode, x: int) -> ListNode:
        
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
