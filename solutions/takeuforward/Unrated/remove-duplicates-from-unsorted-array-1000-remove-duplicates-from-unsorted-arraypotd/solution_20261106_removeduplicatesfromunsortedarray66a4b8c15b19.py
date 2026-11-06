class Solution:
    def removeDuplicates(self, arr):
        seen = set()
        res = []

        for num in arr:
            if num not in seen:
                seen.add(num)
                res.append(num)

        return res

        # return list(dict.fromkeys(arr))
        # dict.fromkeys() creates a dictionary with array elements as keys, naturally stripping duplicates while keeping their first occurrence order.
        # O(N) Time | O(N) Space
