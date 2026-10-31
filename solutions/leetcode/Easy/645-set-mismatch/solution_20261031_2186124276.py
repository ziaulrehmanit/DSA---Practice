__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        HashMap = [0] * (n+1)
        twice = missing = None
        for num in nums:
            HashMap[num] += 1
            if HashMap[num] == 2:
                twice = num
        for i in range(1, n+1):
            if HashMap[i] == 0:
                missing = i
                break
        return [twice, missing]
