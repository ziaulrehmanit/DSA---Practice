'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        closest = float('inf')
        curr = root

        while curr:
            closest = min(closest, abs(curr.data - k))

            if curr.data == k:
                return 0
                
            elif k < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return closest
