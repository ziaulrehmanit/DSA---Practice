class Solution:
    def maxConsecutiveOnes(self, n):
        
        max_count=count=0
        while n>0:
            if n & 1:
                count+=1
                if count > max_count:
                    max_count=count
            else:
                count=0
            n=n>>1
        return max_count
