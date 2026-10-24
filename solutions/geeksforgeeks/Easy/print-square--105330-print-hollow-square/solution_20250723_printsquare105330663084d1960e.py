#User function Template for python3
n = int(input())

# Your code here
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*n)
    else:
        print("* "+'  '*(n-2)+"*")
