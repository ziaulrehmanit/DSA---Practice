def sequence(tup):
    my_list=list(tup)
    d=my_list[1]-my_list[0]
    a1=my_list[0]
    i=0
    while i<3:
        n=len(my_list)+1
        AP=a1+(n-1)*d
        my_list.append(AP)
        i+=1
    return tuple(my_list)    
