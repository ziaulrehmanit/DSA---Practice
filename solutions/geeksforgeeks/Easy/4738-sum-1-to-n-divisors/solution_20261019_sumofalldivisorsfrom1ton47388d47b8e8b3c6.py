class Solution:
    def sumOfDivisors(self, n):
        # Key insight: instead of computing F(i) for every i separately,
        # count how much each number d contributes to the total.
        # A number d is a divisor of i exactly when i is a multiple of d.
        # Within the range 1..n, the multiples of d are d, 2d, 3d, ...,
        # and there are floor(n / d) of them.
        # So d is added floor(n / d) times to the overall sum.
        #
        # Therefore: answer = sum over d = 1..n of d * floor(n / d)

        total = 0
        d = 1

        # Optimization: floor(n / d) takes only O(sqrt(n)) distinct values.
        # For a fixed d, let q = n // d. Every d' in [d, n // q] gives the
        # same quotient q, so we can handle that whole block in one step
        # instead of looping through each d' individually.
        while d <= n:
            q = n // d          # shared quotient for this block
            last = n // q       # largest d' with n // d' == q

            # Sum of integers from d to last (arithmetic series):
            # (count of terms) * (first + last) / 2
            block_sum = (last - d + 1) * (d + last) // 2

            # Each d' in the block contributes d' * q, so the block
            # contributes q * (sum of d' in the block).
            total += q * block_sum

            # Jump to the start of the next block.
            d = last + 1

        return total
