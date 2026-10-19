class Solution:
    def countOccurence(self,arr, k):
        
        HashMap = {}
        
        for value in arr:
            if value in HashMap:
                HashMap[value] += 1
            else:
                HashMap[value] = 1
            
        k = len(arr) // k
        count = 0
        
        for num in HashMap:
            if HashMap[num] > k:
                count += 1
                
        return count
