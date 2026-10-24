class Solution:
    def isPerfect(self, n):
        sum=1
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                if i*i!=n:
                    sum+=i+n//i
                else:
                    sum+=i
        if sum==n and n!=1:
            return True
        else:
            return False
