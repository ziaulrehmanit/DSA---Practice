from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result=[]
        count=Counter(nums1)
        for num in nums2:
            if count[num]>0:
                result.append(num)
                count[num]-=1
        return result
