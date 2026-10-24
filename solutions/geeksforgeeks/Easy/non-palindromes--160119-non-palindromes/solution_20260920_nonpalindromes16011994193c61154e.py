def nonPalindromic(n):
    if n < 0:
        return -1
    elif n < 10:
        return 0
    
    def palindrome(num):
        rev = 0
        dup = num
        while dup > 0:
            rev = (rev * 10) + (dup % 10)
            dup //= 10
        return rev == num
    
    cnt = 0
    for i in range(10, n+1):
        if palindrome(i):
            cnt += 1
            
    return n - cnt - 9
