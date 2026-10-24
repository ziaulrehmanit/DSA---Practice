'''
structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def insertInMiddle(self, head, x):
        
        newNode = Node(x)
        
        if head is None:
            return newNode
        
        slow = head
        fast = head.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        newNode.next = slow.next
        slow.next = newNode
        
        return head
