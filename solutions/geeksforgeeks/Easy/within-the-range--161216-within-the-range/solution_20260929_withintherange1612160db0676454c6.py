#Complete this function
#n is the argument
#The return value is boolean: True/False
def withinTheRange(n):
    #Return True or False according to the n
    i = n - 3
    j = n + 3
    while i <= j:
        if i % 10 == 0:
            return True
        i += 1
    return False
