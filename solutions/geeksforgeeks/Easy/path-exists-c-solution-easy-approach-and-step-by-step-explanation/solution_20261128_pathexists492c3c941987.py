from collections import deque

class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        if u == v:
            return True

        visited = [False] * len(adj)
        visited[u] = True
        queue = deque([u])

        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor == v:
                    return True
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False
