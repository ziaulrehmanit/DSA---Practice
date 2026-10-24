'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        i, j = 0, len(arr)-1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
