import math

class Solution:
    def quadraticRoots(self, a, b, c):
        # Normalize so a > 0. Multiplying the whole equation by -1 keeps the
        # roots unchanged and makes floor division behave predictably below.
        if a < 0:
            a, b, c = -a, -b, -c

        # Discriminant decides the nature of the roots (all-integer arithmetic).
        d = b * b - 4 * a * c

        # Negative discriminant -> imaginary roots; the driver prints "Imaginary".
        if d < 0:
            return [-1]

        # Integer square root: floor(sqrt(d)), exact with no float rounding issues.
        r = math.isqrt(d)

        # Ceiling of sqrt(d): equals r for a perfect square, otherwise r + 1.
        ceil_r = r if r * r == d else r + 1

        denom = 2 * a

        # Larger root = (-b + sqrt(d)) / (2a). Since -b is an integer and denom > 0,
        # floor((-b + sqrt(d)) / denom) == floor((-b + floor(sqrt(d))) / denom).
        larger = (-b + r) // denom

        # Smaller root = (-b - sqrt(d)) / (2a). Subtracting a larger value pushes the
        # result down, so we use ceil(sqrt(d)) to get the exact floor.
        smaller = (-b - ceil_r) // denom

        # Roots are already in decreasing order.
        return [larger, smaller]
