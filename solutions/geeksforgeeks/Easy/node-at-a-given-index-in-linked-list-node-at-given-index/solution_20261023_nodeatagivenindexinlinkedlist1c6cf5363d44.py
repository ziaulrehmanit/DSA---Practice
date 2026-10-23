'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''


class Solution:
    def getNode(self, head: 'Node', k: int) -> int:
        
        cnt = 1
        curr = head
        
        while curr:
            if cnt == k:
                return curr.data
                
            cnt += 1
            curr = curr.next
            
        return -1
