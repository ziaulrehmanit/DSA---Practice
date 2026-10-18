class Solution:
    def merge(self, nums, l, mid, r):
        temp=[]
        low=l
        high=mid+1
        while low<=mid and high<=r:
            if nums[low]<=nums[high]:
                temp.append(nums[low])
                low+=1
            else:
                temp.append(nums[high])
                high+=1
        while low<=mid:
            temp.append(nums[low])
            low+=1
        while high<=r:
            temp.append(nums[high])
            high+=1
        for i in range(l,r+1):
            nums[i]=temp[i-l]
 
    def mergeSort(self, nums, l, r):
        
        if l>=r:
            return
        mid=(l+r)//2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid+1, r)
        self.merge(nums, l, mid, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        
        l=0
        r=len(nums)-1
        self.mergeSort(nums, l, r)

        return nums
