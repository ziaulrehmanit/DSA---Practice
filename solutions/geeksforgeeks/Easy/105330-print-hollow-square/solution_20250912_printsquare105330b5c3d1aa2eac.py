def square(s):
    spaces=s-3
    for i in range(1,s+1):
        if i==1 or i==s:
            print('* '*s)
        else:
            print('* ','  '*spaces,'*')
