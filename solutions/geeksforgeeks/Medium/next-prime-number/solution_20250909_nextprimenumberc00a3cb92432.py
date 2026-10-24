def nextPrime(n):
    if n<2:
        return 2
    else:
        while True:
            n+=1
            is_prime=True
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    is_prime=False 
                    break
            if is_prime:
                return n
                break        
        return n            
