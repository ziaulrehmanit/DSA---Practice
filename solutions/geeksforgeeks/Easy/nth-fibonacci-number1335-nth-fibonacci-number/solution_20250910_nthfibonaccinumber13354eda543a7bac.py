class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n<0:
            return 1
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            a=0
            b=1
            sum=0
            for i in range(1,n):
                sum=a+b
                a=b
                b=sum
            return sum    
