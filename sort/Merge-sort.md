# Notice
注意一下合併時的迴圈中止條件

```py
def mergeSortedArray(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right

    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)/2

    leftSubList = mergeSort(arr[:mid])
    rightSubList = mergeSort(arr[mid:])

    return mergeSortedArray(leftSubList, rightSubList)

# test
print mergeSort([3, 2, 1, 4, 5, 8, 0])
print mergeSort([0])
print mergeSort([1, 0])
```