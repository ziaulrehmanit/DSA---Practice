class Solution:
    def leftRotate(self, arr, d):
        
        d%=len(arr)
        def reverse(start, end):
            while start < end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        
        reverse(0,d-1)
        reverse(d,len(arr)-1)
        reverse(0,len(arr)-1)
