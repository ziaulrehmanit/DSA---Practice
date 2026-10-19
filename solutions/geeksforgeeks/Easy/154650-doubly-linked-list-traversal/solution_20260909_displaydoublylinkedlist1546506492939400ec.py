''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        
        curr = head
        forward = []
        while curr.next:
            forward.append(curr.data)
            curr = curr.next
        forward.append(curr.data)
        backward = []
        while curr:
            backward.append(curr.data)
            curr = curr.prev
        return [forward, backward]
