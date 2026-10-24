class Solution:
    def isAutomorphic(self, n):
        return "Automorphic" if str(n ** 2).endswith(str(n)) else "Not Automorphic"
