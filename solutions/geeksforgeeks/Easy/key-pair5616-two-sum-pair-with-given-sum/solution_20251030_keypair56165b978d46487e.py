def pair_sum(arr, sum):
    set1=set({})
    res=False
    for j in range(len(arr)):
        if (sum-arr[j]) in set1:
            res = True
            break
        else:
            set1.add(arr[j])
    return res       
