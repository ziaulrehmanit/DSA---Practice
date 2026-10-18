class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        preMap = {0 : 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            count += preMap.get(current_sum - k, 0)
            preMap[current_sum] = preMap.get(current_sum, 0) + 1
        
        return count
