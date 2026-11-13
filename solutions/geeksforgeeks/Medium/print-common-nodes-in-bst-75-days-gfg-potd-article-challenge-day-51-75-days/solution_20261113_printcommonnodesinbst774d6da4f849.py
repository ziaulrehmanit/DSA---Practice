''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        s1, s2 = [], []
        res = []

        while True:
            if r1:
                s1.append(r1)
                r1 = r1.left
            elif r2:
                s2.append(r2)
                r2 = r2.left
            elif s1 and s2:
                r1 = s1[-1]
                r2 = s2[-1]

                if r1.data == r2.data:
                    res.append(r1.data)
                    s1.pop()
                    s2.pop()
                    r1 = r1.right
                    r2 = r2.right
                elif r1.data < r2.data:
                    s1.pop()
                    r1 = r1.right
                    r2 = None
                else:
                    s2.pop()
                    r2 = r2.right
                    r1 = None
            else:
                break

        return res
