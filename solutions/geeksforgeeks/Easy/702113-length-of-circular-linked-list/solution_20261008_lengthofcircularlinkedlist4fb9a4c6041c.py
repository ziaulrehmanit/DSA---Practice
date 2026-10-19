''' Linked List Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def getLength(self, head):
        
        size = 0
        curr = head
        while curr:
            size += 1
            if curr.next == head:
                break
            curr = curr.next
        return size
