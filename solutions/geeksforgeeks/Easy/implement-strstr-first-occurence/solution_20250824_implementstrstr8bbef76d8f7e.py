def findPattern(s,p):
    if p in s:
        return s.index(p)
    else:
        return -1
