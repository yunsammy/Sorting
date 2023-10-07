import randarr

arr = randarr.array

count = 0

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)

def partition(arr, p, r):
    s = p-1

    for b in range(p, r):
        global count # 핵심 명령문의 수행횟수
        count += 1 # 핵심 명령문의 수행횟수
        if arr[b] < arr[r]: # 핵심 명령문
            s += 1
            arr[s], arr[b] = arr[b], arr[s]

    q = s+1
    arr[q], arr[r] = arr[r], arr[q]

    return q

quick_sort(arr, 0, len(arr)-1)
print(arr)
print('count:', count)