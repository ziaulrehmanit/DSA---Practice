import math
def firstDigit(n):
    if n<0:
        return n
    else:
        digits=int(math.log10(n))
        F_digit=n//10**digits
        return F_digit
