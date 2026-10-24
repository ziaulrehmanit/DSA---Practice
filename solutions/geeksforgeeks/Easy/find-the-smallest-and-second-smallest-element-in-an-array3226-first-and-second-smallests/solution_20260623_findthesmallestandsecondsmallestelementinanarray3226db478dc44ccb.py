class Solution:
    def minAnd2ndMin(self, arr):
        
        if len(arr) < 2:
            return [-1]
        
        small1 = small2 = 1000000
        for num in arr:
            if num < small1:
                small2 = small1
                small1 = num
            elif small1 < num <small2:
                small2 = num
        if small2 == 1000000:
            return [-1]
        return [small1, small2]
