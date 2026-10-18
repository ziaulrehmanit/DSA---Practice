class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini = min(nums1)
        #Minimum is odd
        if mini & 1:
            return True
        for num in nums1:
            #To turn an odd number into an even number, you have to subtract a smaller odd number from it (Odd - Odd = Even). But because the smallest number in the whole array (mini) is even, the smallest odd number in your array has nothing smaller than itself to subtract from
            if num & 1:
                return False
        return True     #All even
