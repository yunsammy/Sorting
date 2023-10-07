import randarr

arr = randarr.array

count = 0

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i-1
        while (arr[i] < arr[j] and j >= 0): # 핵심 명령문
            global count # 핵심 명령문의 수행횟수
            count += 1   # 핵심 명령문의 수행횟수
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1
            j -= 1


insertion_sort(arr)
print(arr)
print('count:', count)