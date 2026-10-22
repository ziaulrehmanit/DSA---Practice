class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        product = a * b
        while b:
            a, b = b, a % b
        return [product//a, a]
