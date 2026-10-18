# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertAtKthPosition(self, head, X, k):
        if k < 1:
            return head

        node = ListNode(X)
        if k == 1:
            node.next = head
            return node

        n = 1
        curr = head
        while curr and n+1 < k:
            curr = curr.next
            n += 1

        if curr is None:
            return head

        node.next = curr.next
        curr.next = node

        return head
