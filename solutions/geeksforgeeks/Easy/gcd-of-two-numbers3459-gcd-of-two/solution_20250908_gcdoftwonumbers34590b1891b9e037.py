def gcd(a, b):
    minimum=min(a,b)
    res=1
    for i in range(2,minimum+1):
        if a%i==0 and b%i==0:
            res=i
            for j in range(i+1,minimum+1):
                if a%j==0 and b%j==0:
                   res=j
                   for k in range(j+1,minimum+1):
                       if a%k==0 and b%k==0:
                           res=k
    return res                       
