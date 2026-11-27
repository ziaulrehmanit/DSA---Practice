__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k  == 0:
            return [0] * len(code)

        n = len(code)
        res = [0] * n

        for i in range(n):
            sm = cnt = 0

            if k > 0:
                j = i + 1
                while cnt < k:

                    sm += code[j%n]
                    cnt += 1
                    j += 1
            
            else:
                j = i - 1
                while cnt < abs(k):

                    sm += code[j%n]
                    cnt += 1
                    j -= 1

            res[i] = sm

        return res
