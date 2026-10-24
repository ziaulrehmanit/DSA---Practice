def find_minimum(a, b):
    res1=a+b
    res2=a-b
    res3=a*b
    res4=0
    try:
        res4=a/b
    except ZeroDivisionError:
        pass
        
    return min(res1,res2,res3,res4)
