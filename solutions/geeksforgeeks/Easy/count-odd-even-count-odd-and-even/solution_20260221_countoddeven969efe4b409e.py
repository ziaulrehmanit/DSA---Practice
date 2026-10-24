class Solution:
    def countOddEven(self, arr):
        
        oddCount=0
        evenCount=0
        for num in arr:
            if num%2!=0:
                oddCount+=1
            else:
                evenCount+=1
        return oddCount,evenCount
