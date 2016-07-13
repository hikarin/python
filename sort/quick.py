import random

def quick_sort(arr, start, end):
    if start >= end:
        return
    piv_pos = end
    pivot = arr[piv_pos]
    smaller = start
    greater = end
    while(True):
        while(arr[smaller] < pivot and smaller < end):
            smaller += 1
        while(arr[greater] > pivot and greater > start):
            greater -= 1

        if( greater > smaller ):
            if( arr[greater] < arr[smaller] ):
                #swap arr[greater] and arr[smaller]
                tmp = arr[greater]
                arr[greater] = arr[smaller]
                arr[smaller] = tmp
            else:
                #scan continued
                smaller += 1
                greater -= 1
        else:
            #swap arr[smaller-1] and arr[start]
            if arr[smaller] > arr[piv_pos]:
                tmp = arr[smaller-1]
                arr[smaller-1] = arr[piv_pos]
                arr[piv_pos] = tmp
            break

    quick_sort(arr, start, smaller-1)
    quick_sort(arr, greater+1, end)

arr = [random.randint(0, 100) for x in range(50)]

print arr
quick_sort(arr, 0, len(arr)-1)
print arr
