class Solution:
    def removeDuplicates(self, arr):
        
        i=0
        
        for j in range(1,len(arr)):
            
            if arr[j]!=arr[i]:

                 arr[i+1]=arr[j]
                 i+=1

        i+=1
        return arr[:i]
