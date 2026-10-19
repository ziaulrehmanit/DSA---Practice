'''
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def areIdentical(self, head1, head2):
        
        curr1 = head1
        curr2 = head2
        while curr1 and curr2:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1 is None and curr2 is None
