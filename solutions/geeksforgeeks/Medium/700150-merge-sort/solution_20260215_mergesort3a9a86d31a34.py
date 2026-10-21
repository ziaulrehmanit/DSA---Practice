class Solution:
    
    def merge(self, arr, l, mid, r):
        temp=[]
        low=l
        high=mid+1
        while low<=mid and high<=r:
            if arr[low]<=arr[high]:
                temp.append(arr[low])
                low+=1
            else:
                temp.append(arr[high])
                high+=1
        while low<=mid:
            temp.append(arr[low])
            low+=1
        while high<=r:
            temp.append(arr[high])
            high+=1
        for i in range(l,r+1):
            arr[i]=temp[i-l]
 
    def mergeSort(self, arr, l, r):
        
        if l>=r:
            return
        mid=(l+r)//2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        self.merge(arr, l, mid, r)
