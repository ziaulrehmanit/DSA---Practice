class Solution:
    def reverseStack(self, stack):
        
        def insert_at_bottom(item):
            # Base case: empty stack, so item becomes the bottom
            if not stack:
                stack.append(item)
                return
            top = stack.pop()          # hold the top element
            insert_at_bottom(item)     # push item below it
            stack.append(top)          # restore the held element

        def reverse():
            if not stack:
                return
            top = stack.pop()          # remove the top
            reverse()                  # reverse the remaining stack
            insert_at_bottom(top)      # put the old top at the bottom

        reverse()
