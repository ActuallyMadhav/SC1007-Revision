def mergeSort(aList):
    if len(aList) < 2:
        return aList
    
    mid = len(aList) // 2

    firstHalf = aList[:mid]
    secondHalf = aList[mid:]

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

    if leftHalf:
        results.extend(leftHalf)
    if rightHalf:
        results.extend(rightHalf)

    return results

import random
testList = list(range(1,101))
random.shuffle(testList)
print(testList)
print()
sortedList = mergeSort(testList)
print(sortedList)
