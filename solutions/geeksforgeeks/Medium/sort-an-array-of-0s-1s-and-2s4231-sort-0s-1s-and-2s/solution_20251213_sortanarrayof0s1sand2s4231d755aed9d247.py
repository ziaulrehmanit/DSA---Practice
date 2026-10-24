class Solution:
    def sort012(self, arr):
        
        start=mid=0
        end=len(arr)-1
        
        while (mid<=end):
            
            if (arr[mid]==0):
                arr[start],arr[mid]=arr[mid],arr[start]
                mid+=1
                start+=1
                
            elif (arr[mid]==1):
                mid+=1
                
            else:
                arr[end],arr[mid]=arr[mid],arr[end]
                end-=1
                
        return arr
