import random

def insertion_sort(arr):
    print arr
    for x in range(1,len(arr)):
        tmp = arr[x]
        if(arr[x-1] > tmp):
            y = x
            while(True):
                arr[y] = arr[y-1]
                y -= 1
                if( not (y > 0 and arr[y-1] > tmp) ):
                    break
            arr[y] = tmp

arr = [random.randint(0, 100) for x in range(10)]
print arr
insertion_sort(arr)
print arr
