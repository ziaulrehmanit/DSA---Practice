class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        
        freq = {}
        duplicate = n
        while duplicate > 0:
            digit = duplicate % 10
            if digit not in freq:
                freq[digit] = 1
            else:
                freq[digit] += 1
            duplicate //= 10
        score = 0
        for digit, count in freq.items():
            score += digit * count
        return score
