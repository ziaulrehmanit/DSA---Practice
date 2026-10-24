class Solution:
    def missingNum(self, arr):
        

        missing=len(arr)+1
        for i in range (1,len(arr)+1):
            missing^=(i^arr[i-1])
        return missing
