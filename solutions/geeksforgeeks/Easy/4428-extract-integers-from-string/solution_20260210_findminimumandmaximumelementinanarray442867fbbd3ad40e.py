class Solution:
    def getMinMax(self, arr):
        
        minimum=maximum=arr[0]
        for number in range(1,len(arr)):
            if arr[number]>maximum:
                maximum=arr[number]
            if arr[number]<minimum:
                minimum=arr[number]
        return [minimum,maximum]
