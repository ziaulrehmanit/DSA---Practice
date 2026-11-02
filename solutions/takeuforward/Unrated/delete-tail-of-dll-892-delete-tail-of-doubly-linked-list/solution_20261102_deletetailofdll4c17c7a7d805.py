"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteTail(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return None

        curr = head
        while curr.next.next:
            curr = curr.next

        curr.next.prev = None
        curr.next = None

        return head
