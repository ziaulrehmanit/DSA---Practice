class Solution:
    def commonElements(self, a, b, c):
        res = []
        i = j = k = 0
        while i < len(a) and j < len(b) and k < len(c):
            if a[i] == b[j] == c[k] and (not res or res[-1] != a[i]):
                res.append(a[i])
                i += 1
                j += 1
                k += 1
            else:
                mini = min(a[i], b[j], c[k])
                
                if mini == a[i]:
                    i += 1
                if mini == b[j]:
                    j += 1
                if mini == c[k]:
                    k += 1
        return res
