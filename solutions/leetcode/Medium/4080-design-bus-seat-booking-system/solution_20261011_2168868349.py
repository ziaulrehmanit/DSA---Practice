class BusBooking:

    def __init__(self, n: int):
        self.booked_seats = {}
        self.all_time = 0
        self.min_time = 0

    def toggle(self, seat: str) -> None:
        if seat in self.booked_seats:
            self.all_time -= self.booked_seats[seat]
            self.min_time -= 1
            del self.booked_seats[seat]
            return

        
        row_num = seat[1:]
        seat_type = seat[0]
        cost = 1
        if seat_type == 'A':
             if f"B{row_num}" in self.booked_seats:
                 cost = 3
        elif seat_type == 'D':
             if f"C{row_num}" in self.booked_seats:
                 cost = 3

        self.booked_seats[seat] = cost
        self.all_time += cost
        self.min_time += 1
        
    def getTotalTime(self) -> int:
        return self.all_time

    def getMinTime(self) -> int:
        return self.min_time

# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()
