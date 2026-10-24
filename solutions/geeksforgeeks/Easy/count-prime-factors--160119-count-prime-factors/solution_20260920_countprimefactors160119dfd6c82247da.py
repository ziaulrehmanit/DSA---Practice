def primeDivisorsCount(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if n < 0:
        return -1
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if isPrime(i):
                cnt += 1
            if isPrime(n//i):
                cnt += 1
    return cnt
