import randarr

arr = randarr.array

count = 0

def gap_insertion_sort(arr, start, gap):
    n = len(arr)

    for i in range(start+gap, n, gap):
        j = i-gap
        
        while (arr[i] < arr[j] and j >= 0):
            global count
            count += 1
            arr[i], arr[j] = arr[j], arr[i]
            i -= gap
            j -= gap

def shell_sort(arr):
    n = len(arr)

    for gap in range(n//2, 0, -1):
        for s in range(gap):
            gap_insertion_sort(arr, s, gap)

shell_sort(arr)
print(arr)
print('count:', count)