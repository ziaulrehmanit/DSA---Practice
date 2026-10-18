class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ind = ones = -1
        m, n = len(mat), len(mat[0])
        for i in range(m):
            cnt = sum(mat[i])
            if cnt > ones:
                ones = cnt
                ind = i
        return [ind, ones]
