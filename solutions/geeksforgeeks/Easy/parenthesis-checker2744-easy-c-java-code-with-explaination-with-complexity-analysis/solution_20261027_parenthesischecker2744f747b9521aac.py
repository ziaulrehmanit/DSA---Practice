class Solution:
    def isBalanced(self, s):

        if len(s) % 2 == 1:
            return False

        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or brackets[stack[-1]] != char:
                    return False
                stack.pop()

        return not stack
