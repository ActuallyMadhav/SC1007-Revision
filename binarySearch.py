array = [1,4,7,9,19,21,130,200]

def binarySearch(arr, target):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid + 1
    return -1

print(binarySearch(array, 21))