class Solution:
    def reverse(self, arr: List[int], start: int, end: int):

        while start < end:
            arr[start] , arr[end] = arr[end] , arr[start]
            start+=1
            end-=1

        return arr

    def nextPermutation(self, nums: List[int]) -> None:
        
        n = len(nums) - 2
        ind = -1

        for i in range(n, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break

        if ind == -1:
            self.reverse(nums, 0, n+1)
            return

        for i in range(n+1, -1, -1):
            if nums[i] > nums[ind]:
                nums[i] , nums[ind] = nums[ind] , nums[i]
                break

        self.reverse(nums, ind+1, n+1)
