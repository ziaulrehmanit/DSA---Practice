class Solution:
    def medianOf2(self, a, b):
        n = len(a) + len(b)
        ind1, ind2 = n//2 - 1, n//2

        i = j = count = 0
        e1 = e2 = 0

        while count <= ind2:
            if i < len(a) and (j == len(b) or a[i] <= b[j]):
                cur = a[i]
                i += 1
            else:
                cur = b[j]
                j += 1

            if count == ind1:
                e1 = cur
            if count == ind2:
                e2 = cur

            count += 1

        return (e1 + e2) / 2
