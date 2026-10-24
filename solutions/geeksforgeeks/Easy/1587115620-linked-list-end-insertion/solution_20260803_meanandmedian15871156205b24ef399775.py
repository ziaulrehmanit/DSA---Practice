import math
class Solution:
    def median(self, arr):
        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            return arr[(n // 2)]
        return math.floor((arr[(n // 2)] + arr[((n-1) // 2)]) / 2)
    
    def mean(self, arr):
        return math.floor(sum(arr) / len(arr))
