class Solution:
    def smallestSumSubarray(self, A, N):
        
        mini = float('inf')
        sum = 0

        for num in A:

            sum += num

            if sum < mini:
                mini = sum
                
            if sum > 0:
                sum = 0

        return mini
