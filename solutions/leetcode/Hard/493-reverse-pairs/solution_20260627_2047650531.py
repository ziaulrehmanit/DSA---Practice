class Solution:
    def merge_sort(self, arr: List[int]):

        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, left_count = self.merge_sort(arr[:mid])
        right, right_count = self.merge_sort(arr[mid:])

        merged, merged_count = self.merge(left, right)

        total = left_count + right_count + merged_count

        return merged, total

    def merge(self, left: List[int], right: List[int]):

        count = 0
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            count += j
        
        i = j = 0
        sorted_array = []

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array, count

    def reversePairs(self, nums: List[int]) -> int:
        
        sorted_array, count = self.merge_sort(nums)
        return count
