class Solution:
    def segregateElements(self, arr):
        cnt = 0
        for num in arr:
            if num < 0:
                cnt += 1
        pos = 0
        neg = len(arr) - cnt
        ans = [0] * (len(arr))
        for num in arr:
            if num < 0:
                ans[neg] = num
                neg += 1
            else:
                ans[pos] = num
                pos += 1
        for i in range(len(arr)):
            arr[i] = ans[i]
