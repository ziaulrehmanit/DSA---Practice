class Solution:
    def findEvenOccurrences(self, arr):
        
        HashMap = {}
        
        for num in arr:
            
            if num in HashMap:
                HashMap[num] += 1
            else:
                HashMap[num] = 1
                
        res = []
        
        for value in HashMap:
            
            if HashMap[value] % 2 == 0:
                res.append(value)
                
        return res if len(res) != 0 else [-1]
