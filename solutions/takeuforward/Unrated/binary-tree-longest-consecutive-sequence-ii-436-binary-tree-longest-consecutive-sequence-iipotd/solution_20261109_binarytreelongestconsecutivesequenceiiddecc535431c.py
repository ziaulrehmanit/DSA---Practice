# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestConsecutive(self, root):
        self.max_length = 0
        
        def dfs(node):
            if not node:
                return 0, 0  # (increasing_length, decreasing_length)
            
            # Base case values for the current node itself
            curr_inc = 1
            curr_dec = 1
            
            # Traverse left and right subtrees
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            
            # Check relation with the left child
            if node.left:
                if node.left.val == node.val + 1:
                    curr_inc = max(curr_inc, left_inc + 1)
                elif node.left.val == node.val - 1:
                    curr_dec = max(curr_dec, left_dec + 1)
                    
            # Check relation with the right child
            if node.right:
                if node.right.val == node.val + 1:
                    curr_inc = max(curr_inc, right_inc + 1)
                elif node.right.val == node.val - 1:
                    curr_dec = max(curr_dec, right_dec + 1)
            
            # The longest path through the current node combines 
            # one increasing sequence and one decreasing sequence.
            # We subtract 1 because the current node is counted in both.
            self.max_length = max(self.max_length, curr_inc + curr_dec - 1)
            
            return curr_inc, curr_dec

        dfs(root)
        return self.max_length
