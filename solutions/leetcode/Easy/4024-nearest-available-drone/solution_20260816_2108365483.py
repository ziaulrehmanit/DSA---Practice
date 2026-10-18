class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        mini_d = float('+inf')
        ind = -1
        n = len(drones)
        for i in range(n):
            d = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
            if d <= drones[i][2]:
                if d < mini_d:
                    mini_d = d
                    ind = i
        return ind
