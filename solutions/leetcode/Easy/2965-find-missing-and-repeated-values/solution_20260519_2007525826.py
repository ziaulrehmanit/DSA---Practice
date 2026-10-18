class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n2 = n * n

        S = SN = 0
        S2 = SN2 = 0

        SN = (n2 * (n2 + 1)) // 2
        SN2 = (n2 * (n2 + 1) * (2 * n2 + 1)) // 6

        for i in range(n):
            for j in range(n):

                S += grid[i][j]
                S2 += (grid[i][j] * grid[i][j])
        
        val1 = S - SN
        val2 = S2 - SN2
        val2 = val2 // val1

        x = (val1 + val2) // 2
        y = x - val1

        return [x, y]
