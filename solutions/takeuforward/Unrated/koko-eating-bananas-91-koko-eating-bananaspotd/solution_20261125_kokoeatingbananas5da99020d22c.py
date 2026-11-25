class Solution:
    def minimumRateToEatBananas(self, piles, h):
        left, right = 1, max(piles)

        def allBananasEaten(mid):
            hours_needed = 0

            for bananas in piles:
                hours_needed += (bananas // mid)
                hours_needed += 1 if bananas % mid != 0 else 0

                if hours_needed > h:
                    return False

            return True

        while left <= right:
            mid = (left + right) // 2

            if allBananasEaten(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
