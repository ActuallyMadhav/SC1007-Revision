def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

# Example usage
n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = first_occurrence(arr, x)
print(result)
