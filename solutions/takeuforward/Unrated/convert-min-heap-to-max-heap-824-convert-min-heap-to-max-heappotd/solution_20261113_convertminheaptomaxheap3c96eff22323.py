class Solution:
    def minToMaxHeap(self, nums):
        n = len(nums)
        
        def max_heapify(i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
                
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                max_heapify(largest)
                
        for i in range((n - 2) // 2, -1, -1):
            max_heapify(i)
            
        return nums
