class Solution:

    def merge_sort(self, arr):
        # Base case
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        # Sort left and right halves
        left, left_count = self.merge_sort(arr[:mid])
        right, right_count = self.merge_sort(arr[mid:])

        # Merge and count cross inversions
        merged, merge_count = self.merge(left, right)

        total_count = left_count + right_count + merge_count

        return merged, total_count

    def merge(self, left, right):
        i = j = 0
        count = 0
        merged = []

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])

                # All remaining elements in left
                # form inversions with right[j]
                count += len(left) - i

                j += 1

        # Add remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, count

    def inversionCount(self, arr):
        sorted_arr, count = self.merge_sort(arr)
        return count
