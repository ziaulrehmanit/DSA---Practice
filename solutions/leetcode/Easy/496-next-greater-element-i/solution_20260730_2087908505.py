class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                l = len(ans)
                if nums1[i] == nums2[j]:
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            ans.append(nums2[k])
                            break
                    if len(ans) > l:
                        l += 1
                        break
                    else:
                        l += 1
                        ans.append(-1)
                        break
        return ans
