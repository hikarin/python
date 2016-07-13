import random
import copy

def merge_sort(arr, start, end):
    mid = (start+end)/2
    if start < end:
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)

    a = 0
    s = start
    e = mid+1
    tmp = [None] * ( end - start + 1 )
    
    while s <= mid and e <= end:
        if arr[s] < arr[e]:
            tmp[a] = arr[s]
            s += 1
        else:
            tmp[a] = arr[e]
            e += 1
        a += 1
    print tmp[0:a]
            
    if s <= mid:
        tmp[a:] = arr[s:mid+1]
                
    if e <= end:
        tmp[a:] = arr[e:end+1]
                    
    a = 0
    while start <= end:
        arr[start] = tmp[a]
        start += 1
        a += 1

arr = [random.randint(0,100) for x in range(10)]
print arr
merge_sort(arr, 0, len(arr)-1)
print arr
