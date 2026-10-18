class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result=set()
        if len(nums1) <= len(nums2):
            small_array = set(nums1)
            for num in nums2:
                if num in small_array:
                    result.add(num)
        else:
            small_array = set(nums2)
            for num in nums1:
                if num in small_array:
                    result.add(num)
        return list(result)
