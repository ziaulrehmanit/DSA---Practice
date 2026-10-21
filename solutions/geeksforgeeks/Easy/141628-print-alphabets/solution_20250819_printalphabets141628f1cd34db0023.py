#User function Template for python3

def alphabets(c1,c2):
    a=ord(c1)
    b=ord(c2)
    for i in range(a,b+1):
        print(chr(a),end=" ")
        a+=1
