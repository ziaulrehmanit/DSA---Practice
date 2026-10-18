class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        n = len(nums1)
        nums2 = [0] * n
        odd = None
        
        for i in range(n):
            if nums1[i]%2 != 0:
                if odd == None:
                    odd = nums1[i]
                else:
                    odd = min(odd,nums1[i])
                
        for j in range(n):
            if nums1[j]%2 == 0 and odd is not None:
                nums2[j] = nums1[j] - odd
                if nums2[j] <= 0:
                    return False
            else:
                nums2[j] = nums1[j]

        if all(k%2==0 for k in nums2):
            return True
        elif all(k%2!=0 for k in nums2):
            return True
        else:
            return False
