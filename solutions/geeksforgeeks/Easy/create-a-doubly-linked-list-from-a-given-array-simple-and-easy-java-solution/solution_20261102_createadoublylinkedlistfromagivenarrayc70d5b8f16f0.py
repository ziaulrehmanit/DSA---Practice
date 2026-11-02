''' class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

class Solution:
    def createDLL(self, arr):
        
        n = len(arr)
        if n == 0:
            return None

        head = Node(arr[0])
        curr = head
        for i in range(1, n):
            newNode = Node(arr[i])
            curr.next = newNode
            newNode.prev = curr
            curr = curr.next

        return head        
