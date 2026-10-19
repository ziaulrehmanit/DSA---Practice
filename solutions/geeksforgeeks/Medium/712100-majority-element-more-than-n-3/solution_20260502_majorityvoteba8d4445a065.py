class Solution:
    def findMajority(self, arr):
        
        n = len(arr)
        count1 = count2 = 0
        el1 = el2 = None
        
        for num in arr:
            if num == el1:
                count1 += 1
            elif num == el2:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                el1 = num
            elif count2 == 0:
                count2 += 1
                el2 = num
            else:
                count1 -= 1
                count2 -= 1
        
        
        res = []
        count1 = count2 = 0
        
        for num in arr:
            if num == el1:
                count1 += 1
            elif num == el2:
                count2 += 1
                
        if count1 > (n//3):
            res.append(el1)
        if count2 > (n//3):
            res.append(el2)
            
        if len(res) == 2:
            if res[0] > res[1]:
                res[0] , res[1] = res[1] , res[0]
        
        return res
