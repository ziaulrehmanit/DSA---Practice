
from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        
        i=0
        while i<len(arr):
            if arr[i]==k:
                return i+1
            i+=1
        return -1
