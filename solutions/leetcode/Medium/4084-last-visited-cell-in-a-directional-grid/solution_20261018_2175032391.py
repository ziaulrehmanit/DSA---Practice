class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        r, c = 0, 0
        visited = {(0, 0)}

        moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        
        while True:
            direction = grid[r][c]
            direction_of_r, direction_of_c = moves[direction]
            next_r, next_c = r + direction_of_r, c + direction_of_c

            if not (0 <= next_r < m and 0 <= next_c < n) or (next_r, next_c) in visited:
                return [r, c]

            r, c = next_r, next_c
            visited.add((r, c))
