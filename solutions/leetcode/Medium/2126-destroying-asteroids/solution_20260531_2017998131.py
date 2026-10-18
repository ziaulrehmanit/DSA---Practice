class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        asteroids.sort()

        for num in asteroids:

            if mass >= num:
                mass += num
            else:
                return False

            if mass >= asteroids[-1]:
                return True
