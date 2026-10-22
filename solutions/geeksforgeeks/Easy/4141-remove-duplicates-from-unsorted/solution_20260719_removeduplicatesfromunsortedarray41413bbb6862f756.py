class Solution:
    def removeDuplicate(self, arr):
        HashMap = {}
        for num in arr:
            if num in HashMap:
                HashMap[num] += 1
            else:
                HashMap[num] = 1
        for i in range(len(arr)-1, -1, -1):
            if HashMap[arr[i]] > 1:
                HashMap[arr[i]] -= 1
                arr.pop(i)
        return arr
