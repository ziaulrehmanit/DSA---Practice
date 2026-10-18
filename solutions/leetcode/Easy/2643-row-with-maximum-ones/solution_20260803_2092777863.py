class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ind = ones = -1
        m, n = len(mat), len(mat[0])
        for i in range(m):
            cnt = 0
            for j in range(n):
                if mat[i][j] == 1:
                    cnt += 1
            if cnt > ones:
                ones = cnt
                ind = i
        return [ind, ones]
