class Solution:
    def generateRow(self, n: int) -> List[int]:

        ans = 1
        row = []
        row.append(ans)

        for col in range(1, n):
            ans *= (n - col)
            ans //= col
            row.append(ans)

        return row

    def generate(self, numRows: int) -> List[List[int]]:

        res = []

        for i in range(1, numRows+1):
            res.append(self.generateRow(i))

        return res
