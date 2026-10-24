class Solution:
    def isSubset(self, a, b):
        
        HashMap = {}
        
        for num in a:
            HashMap[num] = HashMap.get(num, 0) + 1
            
        for num in b:
            if HashMap.get(num, 0) == 0:
                return False
            HashMap[num] -= 1
        
        return True
