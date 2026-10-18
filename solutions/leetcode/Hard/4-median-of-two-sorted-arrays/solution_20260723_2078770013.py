class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:

        n = len(a) + len(b)
        ind1, ind2 = n // 2 - 1, n // 2

        i = j = 0
        count = -1
        e1 = e2 = 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                x = a[i]
                i += 1
            else:
                x = b[j]
                j += 1

            count += 1
            if count == ind1:
                e1 = x
            if count == ind2:
                e2 = x
                break

        while count < ind2 and i < len(a):
            x = a[i]
            i += 1
            count += 1
            if count == ind1:
                e1 = x
            if count == ind2:
                e2 = x
                break

        while count < ind2 and j < len(b):
            x = b[j]
            j += 1
            count += 1
            if count == ind1:
                e1 = x
            if count == ind2:
                e2 = x
                break

        if n % 2:
            return float(e2)
        return (e1 + e2) / 2
