class Solution:
    def getAngle(self, s: str) -> float:
        
        hour, minutes = map(int, s.split(':'))
        hour_angle = (hour % 12) * 30 + (0.5 * minutes)
        minutes_angle = minutes * 6
        difference = abs(hour_angle - minutes_angle)

        return min(difference, 360-difference)
