class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        L = 0
        R = 0
        _ = 0

        for char in moves:
            if char == 'L':
                L += 1
            elif char == 'R':
                R += 1
            else:
                _ += 1

        return abs(L - R) + _
