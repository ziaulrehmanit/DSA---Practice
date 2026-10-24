class Solution:
    def sumExceptFirstLast(self,arr):
        sumOfArray=0
        for i in range(1,len(arr)-1):
            sumOfArray+=arr[i]
        return sumOfArray
