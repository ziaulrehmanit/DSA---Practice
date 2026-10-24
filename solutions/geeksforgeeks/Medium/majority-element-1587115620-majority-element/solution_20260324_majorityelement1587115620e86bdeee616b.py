class Solution:
    def majorityElement(self, arr):
        
        count=0
        for num in arr:
            if count==0:
                candidate=num
            
            if candidate==num:
                count+=1
            else:
                count-=1
        
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        
        return -1
