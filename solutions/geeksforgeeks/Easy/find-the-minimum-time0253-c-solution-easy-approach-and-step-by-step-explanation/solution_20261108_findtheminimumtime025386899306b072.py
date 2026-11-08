class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # Ideal document split for Scanner 1 (rounded down)
        # Using formula: (n * s2) / (s1 + s2)
        k1 = (n * s2) // (s1 + s2)

        # Option A: Scanner 1 takes k1 documents
        docs_s1_A = k1
        docs_s2_A = n - k1
        time_A = max(docs_s1_A * s1, docs_s2_A * s2)

        # Option B: Scanner 1 takes k1 + 1 documents (rounding up)
        if k1 + 1 <= n:
            docs_s1_B = k1 + 1
            docs_s2_B = n - (k1 + 1)
            time_B = max(docs_s1_B * s1, docs_s2_B * s2)

            return min(time_A, time_B)

        return time_A
