def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2

    firstHalf = arr[:mid]
    secondHalf = arr[mid:]

    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)

    return merge(firstHalf, secondHalf)

def merge(leftHalf, rightHalf):
    results = []

    while leftHalf and rightHalf:
        if leftHalf[0] < rightHalf[0]:
            results.append(leftHalf[0])
            leftHalf.pop(0)
        else:
            results.append(rightHalf[0])
            rightHalf.pop(0)
    
    results.extend(rightHalf)
    results.extend(leftHalf)

    return results

import random
testList = list(range(1,101))
random.shuffle(testList)
print(testList)
print()

sortedList = mergeSort(testList)
print(sortedList)
