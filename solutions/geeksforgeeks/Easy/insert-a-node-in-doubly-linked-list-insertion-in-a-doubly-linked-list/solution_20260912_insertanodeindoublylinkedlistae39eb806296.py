''' Structure of Doubly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        
        newNode = Node(x)
        
        if head is None:
            return newNode
        
        ind = 0
        curr = head
        
        while ind < p and curr is not None:
            ind += 1
            curr = curr.next
            
        nextNode = curr.next
        newNode.next = nextNode
            
        if nextNode is not None:
            nextNode.prev = newNode
        
        newNode.prev = curr
        curr.next = newNode
        
        return head
