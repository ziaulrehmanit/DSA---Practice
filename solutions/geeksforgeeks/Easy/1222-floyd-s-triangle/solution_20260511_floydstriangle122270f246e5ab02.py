n = int(input())

value = 1
for i in range(n):
    for j in range(i+1):
        print(value, end=' ')
        value += 1
    print()
