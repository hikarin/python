import random

def bubble_sort(arr, size):
    for n in range(size):
        for m in range(n):
            if arr[n] < arr[m]:
                #swap arr[n] and arr[m]
                tmp = arr[n]
                arr[n] = arr[m]
                arr[m] = tmp

arr = [random.randint(0, 100) for x in range(30)]

print arr
bubble_sort(arr, len(arr))
print arr
