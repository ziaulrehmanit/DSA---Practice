"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        
        newNode = Node(x)
        newNode.next = head
        
        return newNode
