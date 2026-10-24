class Solution:
    def merge_sort(self, arr):
        
        if len(arr) <= 1:
            return arr, 0
            
        mid = len(arr) // 2
        left, left_count = self.merge_sort(arr[:mid])
        right, right_count = self.merge_sort(arr[mid:])
        merged, merged_count = self.merge(left, right)
        total_count = left_count + right_count + merged_count
        
        return merged, total_count
        
    def merge(self, left, right):
        
        count = 0
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                count += len(left) - i
                j += 1    
        sorted_arr = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
                
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr, count
        
    def countRevPairs(self, arr):
        
        sorted_arr, count = self.merge_sort(arr)
        return count
