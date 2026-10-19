'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def count(self, head, key):
        
        current = head
        freq = 0
        
        while current:
            
            if current.data == key:
                freq += 1
                
            current = current.next
            
        return freq
