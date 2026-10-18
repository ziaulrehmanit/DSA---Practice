class Solution:
    def maxDistance(self, moves: str) -> int:

        U_Count = 0
        D_Count = 0
        L_Count = 0
        R_Count = 0
        _Count = 0
        for char in moves:
            if char == 'U':
                U_Count += 1
            elif char == 'D':
                D_Count += 1
            elif char == 'L':
                L_Count += 1
            elif char == 'R':
                R_Count += 1
            else:
                _Count += 1
        return abs(R_Count - L_Count) + abs(U_Count - D_Count) + _Count
