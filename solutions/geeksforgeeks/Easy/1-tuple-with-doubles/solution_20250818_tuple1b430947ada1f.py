def doubleTup(numbers):
    my_list=list(numbers) 
    empty_list=[]
    for i in my_list:
        res=1
        res=i*2
        empty_list.append(res)
    return tuple(empty_list)    
