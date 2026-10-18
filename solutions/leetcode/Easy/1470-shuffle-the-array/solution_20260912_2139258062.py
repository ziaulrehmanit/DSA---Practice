class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        n = len(nums)
        arr = [0] * n
        i, j = 0, n // 2
        ind = 0

        while j < n:
            arr[ind] = nums[i]
            i += 1
            ind += 1
            arr[ind] = nums[j]
            j += 1
            ind += 1

        return arr
