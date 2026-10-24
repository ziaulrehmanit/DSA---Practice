class Solution:
    def search(self, arr, key):
        
        for index, num in enumerate(arr):
            
            if num == key:
                return True
                
        return False
