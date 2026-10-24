class Solution:

    def searchEle(self, arr, x):
        # Return True if x is present
        for num in arr:
            if num == x:
                return True
        return False

    def insertEle(self, arr, y, yi):
        # Insert y at index yi
        if 0 <= yi <= len(arr):
            arr.insert(yi, y)
            return True
        return False

    def deleteEle(self, arr, z):
        # Delete the first occurrence of z
        for i in range(len(arr)):
            if arr[i] == z:
                arr.pop(i)
                return True
        return False
