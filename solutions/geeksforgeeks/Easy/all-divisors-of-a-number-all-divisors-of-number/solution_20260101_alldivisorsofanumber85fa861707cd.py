class Solution:
    def print_divisors(self, N):
        
        for i in range(1,int(N**0.5)+1):
            if N%i==0:
                print(i,end=' ')
                
        for j in range(int(N**0.5),0,-1):
            if N%j==0:
                if j!=N//j:
                    print(N//j,end=' ')
