class Solution:
    def searchRange(self, nums, target):
        first = last = -1

        def bound(isFirst):
            left, right = 0, len(nums)-1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    index = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return index

        first = bound(True)
        if first == -1:
            return [-1, -1]

        last = bound(False)
        return [first, last]
