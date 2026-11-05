from typing import List

class Solution:
    def findTheDistanceValue(
        self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr1.sort()
        arr2.sort()

        distance_value = 0
        j = 0

        for num in arr1:

            lower = num - d
            upper = num + d

            while j < len(arr2) and arr2[j] < lower:
                j += 1

            if j == len(arr2) or arr2[j] > upper:
                distance_value += 1

        return distance_value
