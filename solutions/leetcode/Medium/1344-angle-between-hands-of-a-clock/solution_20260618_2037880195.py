class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour_angle = (hour % 12) * 30 + (0.5 * minutes)
        minutes_angle = minutes * 6
        difference = abs(hour_angle - minutes_angle)

        return min(difference, 360-difference)
