class Solution:
        
    def lcm(self, a, b):
        org_a=a
        org_b=b
        while b!=0:
            temp=b
            b=a%b
            a=temp
            gcd=a
        
        return (org_a//gcd)*org_b
