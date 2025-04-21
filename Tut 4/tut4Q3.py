# this is a binary search to find the minimum value of a cyclically sorted array

def findMin(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= arr[right]:
            right = mid
        else:
            left = mid + 1
    return arr[left]

list1 = [7, 9, 12, 3, 4, 5, 6]

ans = findMin(list1)

print(ans)
        