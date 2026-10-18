class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = 1
        res= [1]

        for i in range(1, rowIndex+1):

            ans *= (rowIndex - i + 1)
            ans //= (i)
            res.append(ans)

        return res
