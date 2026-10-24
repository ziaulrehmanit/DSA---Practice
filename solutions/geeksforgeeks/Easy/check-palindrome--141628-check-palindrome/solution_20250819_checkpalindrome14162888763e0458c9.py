def isPalindrome(s):
    s1=s.upper()
    s2=s1[::-1]
    if s1==s2:
        return True
    else:
        return False
