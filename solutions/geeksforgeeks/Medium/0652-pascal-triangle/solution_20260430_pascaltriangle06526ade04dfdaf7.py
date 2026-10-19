class Solution:
    
    def nthRowOfPascalTriangle(self, n):
        
        ans = 1
        rowElements = []
        rowElements.append(ans)
        
        for col in range(1, n):
            ans = (ans * (n - col)) // col
            rowElements.append(ans)
            
        return rowElements
