class Solution:
    def totalFine(self, date, car, fine):
        total = 0
        for i in range(len(car)):
            if date%2 != car[i]%2:
                total += fine[i]
        return total
