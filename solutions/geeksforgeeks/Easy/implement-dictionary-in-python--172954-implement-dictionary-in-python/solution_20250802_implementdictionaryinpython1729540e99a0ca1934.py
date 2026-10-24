# Taking input and initializing dictionary
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

########### Write your code below ###############
# Insert k,v in my_dict
my_dict[k]=int(v)
# Print Inserted if inserted successfuly
print("Inserted")
########### Write your code above ###############

d = input()

########### Write your code below ###############
# Delete entry with key d from my_dict
if d in my_dict:
    del my_dict[d]
# Print Deleted if deleted successfuly else print -1
    print("Deleted")
else:
    print(-1)
########### Write your code above ###############

p = input()

########### Write your code below ###############
# Print marks of given key p if key present, else print -1
if p in my_dict:
    print("Marks of",p,"is",my_dict[p])
else:
    print(-1)
########### Write your code above ###############
