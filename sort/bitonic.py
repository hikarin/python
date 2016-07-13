import random
import math

arr_size = 20
int_max = 99

def bitonic_sort(up, arr):
    start = 0
    end = len(arr)
    mid = (start+end)/2
    if len(arr) <= 1:
        return arr
    first  = bitonic_sort(True, arr[:mid])
    second = bitonic_sort(False, arr[mid:])
    return bitonic_merge(up, first, second)

def bitonic_merge(up, arr1, arr2):
    dist = len(arr1)
    arr = [None] * (dist*2)
    for x in range(dist):
        if (up == (arr1[x] < arr2[x])):
            arr[x] = arr1[x]
            arr[x+dist] = arr2[x]
        else:
            arr[x] = arr2[x]
            arr[x+dist] = arr1[x]
    if dist > 1:
        new_dist = dist/2
        first  = bitonic_merge(up, arr[:new_dist], arr[new_dist:dist])
        second = bitonic_merge(up, arr[dist:dist+new_dist], arr[dist+new_dist:])
        print first, second
        return first + second
    else:
        return arr

arr = [random.randint(0, int_max) for x in range(arr_size)]

b = False
if ((arr_size - 1 ) & arr_size) != 0:
    b = True
    n = int(math.log(arr_size<<1, 2))

    start = len(arr)
    end   = 2**n
    for x in range(start, end):
        arr.append(int_max)

print arr[0:arr_size]
arr = bitonic_sort(True, arr)
print arr[0:arr_size]
