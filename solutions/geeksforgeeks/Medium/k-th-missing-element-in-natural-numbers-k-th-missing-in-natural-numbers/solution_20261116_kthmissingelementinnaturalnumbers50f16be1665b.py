class Solution:
    def findKthSmall(self, arr, k):
        arr.sort()

        current_ans = k

        for num in arr:
            if num <= current_ans:
                current_ans += 1
            else:
                break

        return current_ans
