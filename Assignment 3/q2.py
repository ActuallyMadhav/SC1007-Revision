def find_smallest_greater(arr, x):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            result = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return result

n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(find_smallest_greater(arr, x))