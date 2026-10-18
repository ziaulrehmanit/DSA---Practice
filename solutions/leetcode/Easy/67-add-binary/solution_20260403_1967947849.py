class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i = len(a) - 1
        j = len(b) - 1
        Sum = 0
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:

            Sum = carry
            if i >= 0:
                Sum += int(a[i])
                i -= 1
            
            if j >= 0:
                Sum += int(b[j])
                j -= 1

            res.append(str(Sum%2))
            carry = Sum // 2

        return ''.join(reversed(res))
