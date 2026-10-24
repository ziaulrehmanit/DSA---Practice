class Solution:
    def intersectSize(self,a, b):
        
        result=0
        set_a=set(a)
        for num in b:
            if num in set_a:
                result+=1
        return result
