a = list(map(int, input().split()))
b = list(map(str, input().split()))
query = list(map(int, input().split()))
my_dict = {}
for i in range(len(a)):
    my_dict[a[i]] = b[i]
        
ans = []
for key in query:
    val = my_dict.get(key,"None")
    ans.append(val)
print(*ans, sep='\n')
