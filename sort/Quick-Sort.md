# Concept
這是 in place 的版本，原則就是選一個 pivot，把小於等於他的移到左邊。注意 pivotIndex 移動的方式。

這邊有個點是，partition 只負責把小於 pivot 的分到他的左邊，並沒有保證左邊這些已經是排序過的。


```py
def partition(arr, begin, end):
    pivotIndex = begin
    pivotValue = arr[pivotIndex]

    for i in range(begin+1, end+1):  # begin + 1 because first element is pivot
        if arr[i] <= pivotValue:
            pivotIndex += 1
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]

    arr[pivotIndex], arr[begin] = arr[begin], arr[pivotIndex]
    return pivotIndex

def _quickSort(arr, begin, end):
    if begin >= end:
        return
    pivotIndex = partition(arr, begin, end)
    _quickSort(arr, begin, pivotIndex-1)
    _quickSort(arr, pivotIndex+1, end)

def quickSort(arr):
    _quickSort(arr, 0, len(arr)-1)


arr = [3, 1, 5, 2, 4]
quickSort(arr)
print arr
```