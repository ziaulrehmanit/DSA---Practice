class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        return a1+(n-1)*(a2-a1)
