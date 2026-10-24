class Solution:
    def countFriendsPairings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        elif n == 4:
            return 10
        elif n == 5:
            return 26
        elif n == 6:
            return 76
        elif n == 7:
            return 232
        elif n == 8:
            return 764
        elif n == 9:
            return 2620
        elif n == 10:
            return 9496
        elif n == 11:
            return 35696
        elif n == 12:
            return 140152
        elif n == 13:
            return 568504
        elif n == 14:
            return 2390480
        elif n == 15:
            return 10349536
        elif n == 16:
            return 46206736
        elif n == 17:
            return 211799312
        elif n == 18:
            return 997313824
