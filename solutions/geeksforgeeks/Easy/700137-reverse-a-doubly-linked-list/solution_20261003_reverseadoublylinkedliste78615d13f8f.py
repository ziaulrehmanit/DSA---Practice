"""
Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # Handle empty list or single-node list
        if not head or not head.next:
            return head

        curr = head
        prev_node = None

        # Traverse and swap next and prev pointers
        while curr is not None:
            # Swap pointers
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp

            # Move prev_node up to track the new head
            prev_node = curr

            # Move forward in the original list (which is now curr.prev)
            curr = curr.prev

        # prev_node now points to the new head of the reversed list
        return prev_node
