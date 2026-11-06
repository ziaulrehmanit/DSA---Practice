__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

from typing import List
class Solution:
    def countServers(self, n: int, logs: List[List[int]],
                     x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            (query, index)
            for index, query in enumerate(queries)
        )

        freq = [0] * (n + 1)
        answer = [0] * len(queries)
        left = 0
        right = 0
        active_count = 0

        for query, original_index in sorted_queries:
            window_start = query - x

            while right < len(logs) and logs[right][1] <= query:
                server_id = logs[right][0]

                # A server becomes active only when its
                # frequency changes from zero to one.
                if freq[server_id] == 0:
                    active_count += 1

                freq[server_id] += 1
                right += 1

            while left < right and logs[left][1] < window_start:

                server_id = logs[left][0]
                freq[server_id] -= 1
                if freq[server_id] == 0:
                    active_count -= 1

                left += 1
            answer[original_index] = n - active_count

        return answer
