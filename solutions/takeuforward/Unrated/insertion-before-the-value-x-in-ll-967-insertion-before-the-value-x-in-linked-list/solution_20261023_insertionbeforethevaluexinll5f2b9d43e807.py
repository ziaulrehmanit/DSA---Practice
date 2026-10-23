# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next
# Definition of singly linked list:

class Solution:
    def insertBeforeX(self, head, X, val):
        if head and head.data == X:
            return ListNode(val, head)

        curr = head
        while curr and curr.next:
            if curr.next.data == X:
                curr.next = ListNode(val, curr.next)
                break
            curr = curr.next

        return head
