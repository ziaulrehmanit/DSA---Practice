class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        sum_map = {}
        ans = []

        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = arr[i] + arr[j]

                if curr_sum not in sum_map:
                    sum_map[curr_sum] = (i, j)
                else:
                    a, b = sum_map[curr_sum]
                    
                    if a != i and a != j and b != i and b != j:
                        candidate = [a, b, i, j]
                        
                        if not ans or candidate < ans:
                            ans = candidate

        return ans if ans else [-1, -1, -1, -1]
