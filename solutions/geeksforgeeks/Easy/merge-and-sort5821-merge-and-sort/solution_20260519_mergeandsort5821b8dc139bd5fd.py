class Solution:
    def mergeNsort(self, arr1, arr2):
        
        combined = arr1 + arr2
        
        unique_elements = set(combined)
        
        result = sorted(unique_elements)
        
        return result
