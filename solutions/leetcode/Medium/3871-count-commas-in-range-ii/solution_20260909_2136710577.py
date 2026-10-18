class Solution:
    def countCommas(self, n: int) -> int:
        
        commas = 0
        m = 1
        while True:

            threshold = 10 ** (3 * m)

            if n < threshold:
                break

            commas += (n - threshold + 1)
            m += 1

        return commas
