def reverseString(s):
    l=[]
    b=len(s)-1
    for i in range(len(s)):
        l.append(s[b])
        b-=1
    l1="".join(l)   
    return l1
